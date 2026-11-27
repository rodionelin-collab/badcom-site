// Приём заявок с формы на badcom.ru. Работает на собственном сервере в РФ.
// Без внешних пакетов, нужен Node.js 22 или новее. Запуск: node zayavki.mjs
//
// Что делает:
//  1) принимает POST /api/zayavka с формы сайта и проверяет данные;
//  2) сохраняет заявку в файл на этом же сервере (папка DATA_DIR);
//  3) отправляет письмо с заявкой на MAIL_TO через почтовый сервер из настроек;
//  4) отправляет уведомление в Telegram (по умолчанию БЕЗ имени, телефона и адреса);
//  5) раз в сутки удаляет заявки старше RETENTION_DAYS дней (по умолчанию 30),
//     как указано в Согласии на обработку персональных данных.

import http from "node:http";
import https from "node:https";
import net from "node:net";
import tls from "node:tls";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));

// ---------- настройки (из переменных окружения, см. .env.example) ----------
const env = (k, d = "") => (process.env[k] ?? d).toString().trim();
const cfg = {
  host: env("HOST", "127.0.0.1"),
  port: Number(env("PORT", "8787")),
  dataDir: env("DATA_DIR", path.join(here, "data")),
  retentionDays: Number(env("RETENTION_DAYS", "30")),
  smtpHost: env("SMTP_HOST"),
  smtpPort: Number(env("SMTP_PORT", "465")),
  smtpMode: env("SMTP_MODE", "tls"), // tls = защищённое соединение (порт 465); plain = без шифрования (только для локального почтового сервера)
  smtpUser: env("SMTP_USER"),
  smtpPass: env("SMTP_PASS"),
  mailFrom: env("MAIL_FROM", env("SMTP_USER")),
  mailTo: env("MAIL_TO", "info@badcom.ru"),
  tgToken: env("TG_BOT_TOKEN"),
  tgChat: env("TG_CHAT_ID"),
  tgApi: env("TG_API_BASE", "https://api.telegram.org").replace(/\/+$/, ""), // можно указать свой шлюз/зеркало вместо api.telegram.org
  tgProxy: env("TG_PROXY"), // http://[логин:пароль@]хост:порт — HTTP-прокси (метод CONNECT). Пусто — напрямую
  tgFull: env("TG_FULL", "false") === "true", // true — отправлять в Telegram имя, телефон и адрес (см. README: это передача данных за границу)
  thanksUrl: env("THANKS_URL", "/spasibo"),
};

fs.mkdirSync(cfg.dataDir, { recursive: true, mode: 0o700 });
const dataFile = path.join(cfg.dataDir, "zayavki.jsonl");

// ---------- вспомогательное ----------
const clean = (v, max) => String(v ?? "").replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, "").trim().slice(0, max);
const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
const log = (...a) => console.log(new Date().toISOString(), ...a); // в журнал персональные данные не пишем

const hits = new Map(); // простая защита от спама: не больше 5 заявок в час с одного адреса
function rateLimited(ip) {
  const now = Date.now();
  const list = (hits.get(ip) || []).filter((t) => now - t < 3600e3);
  list.push(now);
  hits.set(ip, list);
  return list.length > 5;
}

function readBody(req, limit = 20000) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on("data", (c) => {
      size += c.length;
      if (size > limit) { reject(Object.assign(new Error("too large"), { code: 413 })); req.destroy(); return; }
      chunks.push(c);
    });
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}

// ---------- отправка письма (SMTP без внешних пакетов) ----------
function smtpSend({ from, to, subject, text }) {
  return new Promise((resolve, reject) => {
    if (!cfg.smtpHost) return reject(new Error("SMTP не настроен"));
    const socket = cfg.smtpMode === "tls"
      ? tls.connect({ host: cfg.smtpHost, port: cfg.smtpPort, servername: cfg.smtpHost })
      : net.connect({ host: cfg.smtpHost, port: cfg.smtpPort });
    socket.setTimeout(20000, () => { socket.destroy(); reject(new Error("SMTP: таймаут")); });
    socket.on("error", reject);

    let buf = "";
    let waiter = null;
    socket.on("data", (d) => {
      buf += d.toString("utf8");
      const lines = buf.split("\r\n");
      const last = lines.filter(Boolean).at(-1) || "";
      if (buf.endsWith("\r\n") && /^\d{3} /.test(last)) {
        const reply = buf; buf = "";
        if (waiter) { const w = waiter; waiter = null; w(reply); }
      }
    });
    const reply = () => new Promise((r) => { waiter = r; });
    const cmd = async (line, ok) => {
      if (line !== null) socket.write(line + "\r\n");
      const r = await reply();
      if (!ok.some((c) => r.startsWith(c))) throw new Error("SMTP: " + r.trim().slice(0, 200));
      return r;
    };
    const b64 = (s) => Buffer.from(s, "utf8").toString("base64");

    (async () => {
      await cmd(null, ["220"]);
      await cmd("EHLO badcom.ru", ["250"]);
      if (cfg.smtpUser) {
        await cmd("AUTH LOGIN", ["334"]);
        await cmd(b64(cfg.smtpUser), ["334"]);
        await cmd(b64(cfg.smtpPass), ["235"]);
      }
      await cmd(`MAIL FROM:<${from}>`, ["250"]);
      await cmd(`RCPT TO:<${to}>`, ["250", "251"]);
      await cmd("DATA", ["354"]);
      const body = text.replace(/\r?\n/g, "\r\n"); // тело в base64, точки в начале строк не страшны
      const msg = [
        `From: =?UTF-8?B?${b64("Сайт badcom.ru")}?= <${from}>`,
        `To: <${to}>`,
        `Subject: =?UTF-8?B?${b64(subject)}?=`,
        `Date: ${new Date().toUTCString()}`,
        `Message-ID: <${crypto.randomUUID()}@badcom.ru>`,
        "MIME-Version: 1.0",
        "Content-Type: text/plain; charset=UTF-8",
        "Content-Transfer-Encoding: base64",
        "",
        Buffer.from(body, "utf8").toString("base64").replace(/(.{76})/g, "$1\r\n"),
        ".",
      ].join("\r\n");
      await cmd(msg, ["250"]);
      socket.write("QUIT\r\n");
      socket.end();
      resolve();
    })().catch((e) => { socket.destroy(); reject(e); });
  });
}

// ---------- Telegram ----------
// У ошибок сети (например, AggregateError при недоступном адресе) message бывает пустым, поэтому берём код и вложенные причины
function errText(e) {
  const parts = [e.code, e.message].filter(Boolean);
  if (Array.isArray(e.errors)) for (const x of e.errors) parts.push([x.code, x.address && `${x.address}:${x.port}`].filter(Boolean).join(" "));
  return parts.join(" | ") || String(e);
}
// Отправка идёт с этого сервера напрямую на api.telegram.org (или на TG_API_BASE),
// при необходимости через HTTP-прокси TG_PROXY. Сторонних шлюзов в коде нет.
function tgRequest(url, body) {
  return new Promise((resolve, reject) => {
    const u = new URL(url);
    const opts = {
      method: "POST",
      hostname: u.hostname,
      port: u.port || (u.protocol === "https:" ? 443 : 80),
      path: u.pathname + u.search,
      headers: { "content-type": "application/json", "content-length": Buffer.byteLength(body) },
      timeout: 10000,
    };
    const lib = u.protocol === "https:" ? https : http;
    const send = (extra = {}) => {
      const req = lib.request({ ...opts, ...extra }, (res) => { res.resume(); res.on("end", () => resolve(res.statusCode)); });
      req.on("timeout", () => req.destroy(new Error("таймаут")));
      req.on("error", reject);
      req.end(body);
    };
    if (!cfg.tgProxy || u.protocol !== "https:") return send();
    // через HTTP-прокси: просим прокси открыть туннель (CONNECT), дальше обычный HTTPS
    const px = new URL(cfg.tgProxy);
    const headers = { host: `${u.hostname}:${opts.port}` };
    if (px.username) {
      headers["proxy-authorization"] = "Basic " + Buffer.from(`${decodeURIComponent(px.username)}:${decodeURIComponent(px.password)}`).toString("base64");
    }
    const c = http.request({ hostname: px.hostname, port: px.port || 80, method: "CONNECT", path: `${u.hostname}:${opts.port}`, headers, timeout: 10000 });
    c.on("timeout", () => c.destroy(new Error("таймаут прокси")));
    c.on("error", reject);
    c.on("connect", (res, socket) => {
      if (res.statusCode !== 200) { socket.destroy(); return reject(new Error("прокси ответил " + res.statusCode)); }
      send({ createConnection: () => tls.connect({ socket, servername: u.hostname }), agent: false });
    });
    c.end();
  });
}

async function telegram(text) {
  if (!cfg.tgToken || !cfg.tgChat) return;
  const body = JSON.stringify({ chat_id: cfg.tgChat, text, parse_mode: "HTML", disable_web_page_preview: true });
  const code = await tgRequest(`${cfg.tgApi}/bot${cfg.tgToken}/sendMessage`, body);
  if (code !== 200) throw new Error("Telegram: HTTP " + code);
}

// ---------- удаление старых заявок ----------
function purge() {
  if (!fs.existsSync(dataFile)) return;
  const limit = Date.now() - cfg.retentionDays * 86400e3;
  const keep = [];
  let removed = 0;
  for (const line of fs.readFileSync(dataFile, "utf8").split("\n").filter(Boolean)) {
    let fresh = true;
    try { fresh = Date.parse(JSON.parse(line).received) >= limit; } catch { /* битую строку оставляем */ }
    if (fresh) keep.push(line); else removed++;
  }
  fs.writeFileSync(dataFile, keep.length ? keep.join("\n") + "\n" : "", { mode: 0o600 });
  if (removed) log(`Удалено заявок старше ${cfg.retentionDays} дн.: ${removed}`);
}

// ---------- обработка заявки ----------
async function handleZayavka(req, res) {
  const ip = (req.headers["x-forwarded-for"] || req.socket.remoteAddress || "").toString().split(",")[0].trim();
  const form = new URLSearchParams(await readBody(req));

  if (form.get("company_site")) return done(res, 303, cfg.thanksUrl); // заполнено скрытое поле: это робот, ему показываем «спасибо»
  if (rateLimited(ip)) return done(res, 429, null, "Слишком много заявок. Позвоните нам по телефону.");

  const z = {
    id: crypto.randomBytes(4).toString("hex"),
    received: new Date().toISOString(),
    ip,
    name: clean(form.get("name"), 120),
    phone: clean(form.get("phone"), 40),
    district: clean(form.get("district"), 80),
    settlement: clean(form.get("settlement"), 120),
    address: clean(form.get("address"), 250),
    client: clean(form.get("client"), 60),
    message: clean(form.get("message"), 1500),
    page: clean(form.get("page"), 60),
    consent: form.get("consent") ? "да" : "",
    consent_doc: clean(form.get("consent_doc"), 120),
    consent_time: clean(form.get("consent_time"), 40),
  };
  const digits = z.phone.replace(/\D/g, "");
  if (!z.name || !z.address || digits.length < 10 || digits.length > 15) return done(res, 400, null, "Проверьте имя, телефон и адрес.");
  if (!z.consent) return done(res, 400, null, "Нужно согласие на обработку персональных данных.");

  fs.appendFileSync(dataFile, JSON.stringify(z) + "\n", { mode: 0o600 }); // сначала сохраняем: заявка не потеряется, даже если почта не работает
  log("Новая заявка", z.id);

  const text = [
    `Новая заявка с сайта badcom.ru № ${z.id}`,
    "",
    `Имя: ${z.name}`,
    `Телефон: ${z.phone}`,
    `Район: ${z.district || "не указан"}`,
    `Населённый пункт: ${z.settlement || "не выбран"}`,
    `Адрес: ${z.address}`,
    `Кого подключаем: ${z.client}`,
    `Комментарий: ${z.message || "—"}`,
    "",
    `Страница: ${z.page}`,
    `Получена: ${z.received}`,
    `Согласие на обработку ПДн: ${z.consent_doc}, отмечено ${z.consent_time || z.received}`,
  ].join("\n");

  const jobs = [
    smtpSend({ from: cfg.mailFrom, to: cfg.mailTo, subject: `Заявка с сайта № ${z.id}: ${z.name}, ${z.phone}`, text })
      .catch((e) => log("Письмо не отправлено:", e.message)),
    telegram(cfg.tgFull
      ? `<b>Новая заявка № ${z.id}</b>\n${esc(z.name)}\n${esc(z.phone)}\n${esc(z.district)}, ${esc(z.address)}\n${esc(z.client)}\n${esc(z.message)}`
      : `Новая заявка с сайта № ${z.id}. Район: ${esc(z.district || "не указан")}. Подробности в почте ${esc(cfg.mailTo)}.`)
      .catch((e) => log("Telegram не отправлен:", errText(e))),
  ];
  await Promise.all(jobs);
  return done(res, 303, cfg.thanksUrl);
}

function done(res, code, location, message) {
  if (location) { res.writeHead(code, { location }); return res.end(); }
  res.writeHead(code, { "content-type": "text/html; charset=utf-8" });
  res.end(`<!doctype html><meta charset="utf-8"><p>${esc(message || "Ошибка")}</p><p><a href="javascript:history.back()">Вернуться к форме</a></p>`);
}

const server = http.createServer(async (req, res) => {
  try {
    if (req.method === "POST" && req.url === "/api/zayavka") return await handleZayavka(req, res);
    if (req.method === "GET" && req.url === "/api/health") { res.writeHead(200); return res.end("ok"); }
    res.writeHead(404); res.end();
  } catch (e) {
    log("Ошибка:", e.message);
    done(res, e.code === 413 ? 413 : 500, null, "Не удалось отправить заявку. Позвоните нам по телефону.");
  }
});

purge();
setInterval(purge, 24 * 3600e3).unref();
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  server.listen(cfg.port, cfg.host, () => log(`Приём заявок запущен на ${cfg.host}:${cfg.port}`));
}
export { server, purge, cfg };
