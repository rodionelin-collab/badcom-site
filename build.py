# -*- coding: utf-8 -*-
"""Генератор статического сайта badcom.ru. Запуск: python3 build.py -> папка site/"""
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
os.makedirs(OUT, exist_ok=True)

PHONE = "+7 (3952) 798-567"
PHONE_TEL = "+73952798567"
SUPPORT = "+7 939 793-97-14"
SUPPORT_TEL = "+79397939714"
EMAIL = "info@badcom.ru"
LK = "http://lk.badcom.ru/"
TG = "https://t.me/badcom_news"

DISTRICTS = ["Аларский", "Боханский", "Жигаловский", "Заларинский", "Зиминский",
             "Казачинско-Ленский", "Качугский", "Усольский", "Усть-Удинский", "Черемховский"]

PAGES = [  # slug, короткое имя в навигации
    ("index", "Базовые"),
    ("tariff_zone2", "Зона «х2»"),
    ("tariff_sputnik", "Спутник"),
    ("tariff_biz", "Юрлицам"),
    ("tariff_sputnik_biz", "Спутник юрлицам"),
]

def href(slug):
    return "/" if slug == "index" else f"/{slug}"

# ---------- данные тарифов ----------
def unlim(rows):
    return [dict(name=n, price=p, speed=s) for n, p, s in rows]

BASE = unlim([("512/512", 700, "512 Кбит/с"), ("1 Мегабит", 900, "1 Мбит/с"),
              ("2 Мегабита", 1100, "2 Мбит/с"), ("5 Мегабит", 1350, "5 Мбит/с"),
              ("10 Мегабит", 1800, "10 Мбит/с"), ("Максимум", 2800, "до 20 Мбит/с")])
X2 = unlim([("512/512", 1100, "512 Кбит/с"), ("1 Мегабит", 1500, "1 Мбит/с"),
            ("2 Мегабита", 1850, "2 Мбит/с"), ("5 Мегабит", 2350, "5 Мбит/с"),
            ("10 Мегабит", 3300, "10 Мбит/с"), ("Максимум", 5000, "до 20 Мбит/с")])
BIZ = unlim([("512/512", 2000, "512 Кбит/с"), ("1 Мегабит", 2500, "1 Мбит/с"),
             ("2 Мегабита", 3000, "2 Мбит/с"), ("5 Мегабит", 4000, "5 Мбит/с"),
             ("10 Мегабит", 7000, "10 Мбит/с"), ("Максимум", 9500, "до 20 Мбит/с")])

def vol(rows):  # помегабайтные: имя, цена, объём, цена МБ сверх, скорость
    return [dict(name=n, price=p, volume=v, over=o, speed=s) for n, p, v, o, s in rows]

def surf(rows):  # серфинг: имя, цена, сутки, месяц, скорость, после лимита
    return [dict(name=n, price=p, day=d, month=m, speed=s, after=a) for n, p, d, m, s, a in rows]

SAT_VOL = vol([("Помегабайтный", 400, "1,5 ГБ", "20 коп.", "до 1/1 Мбит/с"),
               ("Скорость-3", 1100, "3 ГБ", "16 коп.", "до 2/2 Мбит/с"),
               ("Скорость-5", 1300, "5 ГБ", "15 коп.", "до 5/5 Мбит/с"),
               ("Скорость-10", 1900, "10 ГБ", "14 коп.", "до 5/5 Мбит/с"),
               ("Скорость-15", 2500, "15 ГБ", "13 коп.", "до 5/5 Мбит/с"),
               ("Скорость-20", 4300, "20 ГБ", "12 коп.", "до 5/5 Мбит/с")])
SAT_SURF = surf([("Серфинг-350", 1600, "350 МБ", "~10,5 ГБ", "до 1/1 Мбит/с", "без доступа до следующих суток"),
                 ("Серфинг-500", 1900, "500 МБ", "~15 ГБ", "до 2/2 Мбит/с", "до 64/64 Кбит/с"),
                 ("Серфинг-800", 2500, "800 МБ", "~24 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с")])
TURBO = [("Турбо 500", 200, "500 МБ трафика на скорости вашего тарифа"),
         ("Турбо 1500", 400, "1500 МБ трафика на скорости вашего тарифа"),
         ("Турбо Unlim", 900, "Безлимит на одни сутки на скорости до 1/1 Мбит/с")]

SATB_VOL = vol([("Помегабайтный", 700, "1,5 ГБ", "20 коп.", "до 1/1 Мбит/с"),
                ("Скорость-3", 1600, "3 ГБ", "16 коп.", "до 2/2 Мбит/с"),
                ("Скорость-5", 1900, "5 ГБ", "15 коп.", "до 5/5 Мбит/с"),
                ("Скорость-10", 2700, "10 ГБ", "14 коп.", "до 5/5 Мбит/с"),
                ("Скорость-15", 3500, "15 ГБ", "13 коп.", "до 5/5 Мбит/с"),
                ("Скорость-20", 5900, "20 ГБ", "12 коп.", "до 5/5 Мбит/с")])
SATB_SURF = surf([("Серфинг-350", 2500, "350 МБ", "~10,5 ГБ", "до 1/1 Мбит/с", "без доступа до следующих суток"),
                  ("Серфинг-500", 3300, "500 МБ", "~15 ГБ", "до 2/2 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-800", 4800, "800 МБ", "~24 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-1000", 5900, "1000 МБ", "~30 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-2000", 9500, "2000 МБ", "~60 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с"),
                  ("Серфинг-5000", 18000, "5000 МБ", "~150 ГБ", "до 3/3 Мбит/с", "до 64/64 Кбит/с")])

def rub(n):
    return f"{n:,}".replace(",", " ") + " ₽"

# ---------- фрагменты ----------
CSS = r"""
:root{
  --taiga:#1E3A2F; --taiga-2:#2B4F40; --ink:#15211B; --muted:#56665E;
  --paper:#EEF2EF; --white:#FFFFFF; --line:#C9D4CE; --signal:#F2B705; --signal-ink:#3A2C00;
  --todo:#FFE9A8;
  --r-s:6px; --r-m:14px;
  --wrap:1160px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 "Golos Text",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
:focus-visible{outline:3px solid var(--signal);outline-offset:3px;border-radius:4px}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:"Unbounded",sans-serif;font-weight:600;line-height:1.12;margin:0;letter-spacing:-.01em}
h2{font-size:clamp(26px,3.4vw,40px)}
h3{font-size:19px}
p{margin:0 0 1em;max-width:68ch}
.muted{color:var(--muted)}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:var(--white);padding:8px 12px;z-index:10}

/* header */
.top{background:var(--taiga);color:#E6EEE9}
.top .wrap{display:flex;align-items:center;gap:20px;min-height:72px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.mark{display:flex;flex-direction:column;text-decoration:none;line-height:1.05;margin-right:auto}
.mark b{font-family:"Unbounded",sans-serif;font-weight:700;font-size:19px;color:#fff}
.mark small{font-size:12px;color:#A9BDB2;letter-spacing:.04em}
.nav{display:flex;gap:16px;flex-wrap:wrap}
@media (min-width:901px){.top .wrap{flex-wrap:nowrap}.nav{flex-wrap:nowrap;white-space:nowrap}}
.nav a{text-decoration:none;font-size:15px;color:#D5E1DA}
.nav a:hover{color:#fff;text-decoration:underline;text-underline-offset:4px}
.top .tel{font-weight:600;text-decoration:none;color:#fff;white-space:nowrap}
.btn{display:inline-flex;align-items:center;gap:8px;font:600 16px/1 "Golos Text",system-ui,sans-serif;text-decoration:none;border:0;cursor:pointer;
  padding:14px 20px;border-radius:var(--r-s);white-space:nowrap;background:var(--signal);color:var(--signal-ink)}
.btn:hover{background:#FFC820}
.btn.ghost{background:transparent;color:inherit;box-shadow:inset 0 0 0 2px currentColor}
.btn.ghost:hover{background:rgba(255,255,255,.08)}
.top .btn{padding:11px 16px;font-size:15px}

/* hero */
.hero{background:var(--taiga);color:#EAF1ED;position:relative;overflow:hidden;padding:56px 0 72px}
.hero .wrap{display:grid;grid-template-columns:1.25fr .9fr;gap:48px;align-items:end;position:relative;z-index:1}
.hero h1{font-size:clamp(44px,8.2vw,108px);font-weight:700;line-height:.92;letter-spacing:-.035em;color:#fff}
.hero h1 span{display:block;color:transparent;-webkit-text-stroke:2px #fff}
.hero .lede{font-size:clamp(18px,2vw,21px);margin:28px 0 30px;color:#D3DFD8;max-width:34ch}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap}
.waves{position:absolute;right:-120px;top:-60px;width:760px;height:760px;opacity:.5;pointer-events:none}
.waves circle{fill:none;stroke:#3F6A57;stroke-width:1.5}
.waves .pulse{stroke:var(--signal);stroke-width:2;opacity:0;animation:ping 4.5s ease-out 1}
.waves .pulse:nth-of-type(2){animation-delay:.35s}.waves .pulse:nth-of-type(3){animation-delay:.7s}
@keyframes ping{0%{opacity:0}20%{opacity:.9}100%{opacity:0}}
.where{background:var(--white);color:var(--ink);border-radius:var(--r-m);padding:24px 24px 20px}
.where h2{font-size:18px;margin-bottom:6px}
.where p{font-size:15px;color:var(--muted);margin-bottom:14px}
.where ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:2px 16px}
.where li{padding:7px 0;border-bottom:1px solid #E3E9E5;font-size:15px}
.where li::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--signal);margin-right:10px;vertical-align:1px}

/* page head for tariff pages */
.phead{background:var(--taiga);color:#fff;padding:44px 0 40px}
.phead h1{font-size:clamp(32px,5vw,58px);letter-spacing:-.025em}
.phead p{color:#C9D8CF;margin:14px 0 0}

/* sections */
section{padding:72px 0}
.sec-head{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:28px}
.sec-head p{margin:10px 0 0;color:var(--muted)}

/* service strip */
.strip{background:var(--white);border-bottom:1px solid var(--line);padding:0}
.strip .wrap{display:grid;grid-template-columns:repeat(3,1fr)}
.strip a{display:block;padding:22px 24px;text-decoration:none;border-left:1px solid var(--line)}
.strip a:first-child{border-left:0;padding-left:0}
.strip b{display:block;font-size:17px}
.strip span{font-size:14px;color:var(--muted)}
.strip a:hover b{text-decoration:underline;text-underline-offset:4px}

/* tariff tabs */
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:22px}
.tabs a{padding:9px 15px;border-radius:999px;text-decoration:none;font-size:15px;background:var(--white);box-shadow:inset 0 0 0 1px var(--line)}
.tabs a[aria-current]{background:var(--taiga);color:#fff;box-shadow:none}
.tabs a:not([aria-current]):hover{box-shadow:inset 0 0 0 1px var(--taiga)}

/* tariff table */
.plans{background:var(--white);border-radius:var(--r-m);overflow:hidden}
.plan{display:grid;grid-template-columns:minmax(150px,1fr) 2fr auto;gap:20px;align-items:center;padding:20px 28px;border-top:1px solid #E3E9E5}
.plan:first-child{border-top:0}
.plan .nm{font-family:"Unbounded",sans-serif;font-weight:600;font-size:18px}
.plan .det{font-size:15px;color:var(--muted)}
.plan .det b{color:var(--ink);font-weight:600}
.plan .pr{font-family:"Unbounded",sans-serif;font-weight:600;font-size:24px;white-space:nowrap;text-align:right}
.plan .pr small{display:block;font-family:"Golos Text",system-ui,sans-serif;font-weight:400;font-size:13px;color:var(--muted)}
.bar{height:6px;border-radius:3px;background:#E3E9E5;margin-top:8px;max-width:260px}
.bar i{display:block;height:100%;border-radius:3px;background:var(--taiga-2)}
.plans-cap{font-family:"Unbounded",sans-serif;font-size:17px;font-weight:600;margin:36px 0 12px}

/* conditions */
.cond{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}
.note{background:var(--white);border-radius:var(--r-m);padding:26px 28px}
.note h3{margin-bottom:10px}
.note p{font-size:16px}
.note p:last-child{margin-bottom:0}
.price-big{font-family:"Unbounded",sans-serif;font-weight:700;font-size:40px;line-height:1;margin:6px 0 12px}
.callout{border-left:4px solid var(--signal);background:#FFF8E0;padding:16px 20px;border-radius:0 var(--r-s) var(--r-s) 0;margin-top:20px;font-size:16px}
.callout p{margin:0}

/* faq */
.faq{max-width:840px}
.faq details{border-top:1px solid var(--line)}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:20px 40px 20px 0;font-weight:600;font-size:18px;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";position:absolute;right:6px;top:50%;width:12px;height:12px;border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:translateY(-70%) rotate(45deg);transition:transform .2s}
.faq details[open] summary::after{transform:translateY(-30%) rotate(-135deg)}
.faq .a{padding:0 0 20px}
.todo{background:var(--todo);padding:2px 6px;border-radius:4px}

/* reviews */
.reviews{background:var(--taiga);color:#E6EEE9}
.reviews h2{color:#fff}
.rv{columns:2 340px;column-gap:40px;margin-top:28px}
.rv figure{break-inside:avoid;margin:0 0 36px}
.rv blockquote{margin:0;font-size:17px;line-height:1.6}
.rv figcaption{margin-top:10px;color:var(--signal);font-weight:600}

/* form */
.apply .wrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:start}
form{background:var(--white);border-radius:var(--r-m);padding:28px}
label{display:block;font-weight:600;font-size:15px;margin:0 0 6px}
input,textarea,select{width:100%;font:inherit;padding:12px 14px;border:1px solid var(--line);border-radius:var(--r-s);background:#FBFCFB;margin-bottom:16px;color:var(--ink)}
input:focus,textarea:focus,select:focus{outline:2px solid var(--taiga);border-color:var(--taiga)}
textarea{min-height:96px;resize:vertical}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.consent{display:flex;gap:10px;font-weight:400;font-size:14px;color:var(--muted);align-items:flex-start}
.consent input{width:auto;margin:3px 0 0}
.hp{display:none}
.direct{margin-top:22px}
.direct a{font-weight:600}

/* contacts */
.contacts .wrap{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.hours{font-size:15px;color:var(--muted)}
.docs{list-style:none;margin:0;padding:0}
.docs li{border-top:1px solid #E3E9E5;padding:12px 0}
.docs li:first-child{border-top:0;padding-top:0}
.docs a{font-weight:600}
.docs span{display:block;font-size:14px;color:var(--muted)}
details.req summary{cursor:pointer;font-weight:600;margin-top:16px}
.req dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 18px;font-size:14px;margin:14px 0 0}
.req dt{color:var(--muted)}.req dd{margin:0}

footer{background:var(--ink);color:#A9B8B0;font-size:14px;padding:32px 0}
footer .wrap{display:flex;gap:16px 32px;flex-wrap:wrap;justify-content:space-between}
footer a{color:#D5E1DA}

@media (max-width:900px){
  .hero .wrap,.apply .wrap,.contacts .wrap,.cond{grid-template-columns:1fr}
  .waves{width:520px;height:520px;right:-200px}
  .nav{order:3;width:100%;gap:14px}
  .strip .wrap{grid-template-columns:1fr}
  .strip a,.strip a:first-child{border-left:0;border-top:1px solid var(--line);padding:16px 0}
  .strip a:first-child{border-top:0}
}
@media (max-width:640px){
  .wrap{padding:0 16px}
  body{font-size:16px}
  section{padding:52px 0}
  .plan{grid-template-columns:1fr auto;padding:18px 18px;gap:6px 16px}
  .plan .det{grid-column:1/-1;grid-row:2}
  .plan .pr{grid-row:1;grid-column:2}
  .where ul{grid-template-columns:1fr}
  .row2{grid-template-columns:1fr}
  .top .tel{display:none}
  .req dl{grid-template-columns:1fr}
  .req dd{margin-bottom:6px}
}
"""

def head(title, desc, slug):
    canon = "https://badcom.ru" + ("" if slug == "index" else f"/{slug}")
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta name="format-detection" content="telephone=no">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;600&family=Unbounded:wght@600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Перейти к содержимому</a>
"""

def header(slug):
    pre = "" if slug == "index" else "/"
    return f"""<header class="top">
  <div class="wrap">
    <a class="mark" href="/"><b>Плохая Компания</b><small>badcom.ru</small></a>
    <nav class="nav" aria-label="Разделы">
      <a href="{pre}#tarif">Тарифы</a>
      <a href="{pre}#zona">Где работаем</a>
      <a href="{pre}#faq">Вопросы</a>
      <a href="#contacts">Контакты</a>
      <a href="{TG}" target="_blank" rel="noopener">Канал в Telegram</a>
    </nav>
    <a class="tel" href="tel:{PHONE_TEL}">{PHONE}</a>
    <a class="btn" href="{LK}">Личный кабинет</a>
  </div>
</header>
"""

def tabs(current):
    out = ['<nav class="tabs" aria-label="Тарифные зоны">']
    for slug, label in PAGES:
        cur = ' aria-current="page"' if slug == current else ""
        link = "/#tarif" if slug == "index" else href(slug)
        out.append(f'<a href="{link}"{cur}>{label}</a>')
    out.append("</nav>")
    return "\n".join(out)

SPEED_MAX = {"512 Кбит/с": 0.5, "1 Мбит/с": 1, "2 Мбит/с": 2, "5 Мбит/с": 5, "10 Мбит/с": 10, "до 20 Мбит/с": 20}

def unlim_table(rows):
    out = ['<div class="plans">']
    for r in rows:
        w = max(4, SPEED_MAX[r["speed"]] / 20 * 100)
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det">Безлимит. Скачивание и отдача — <b>{r['speed']}</b><div class="bar" aria-hidden="true"><i style="width:{w:.0f}%"></i></div></div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def vol_table(rows):
    out = ['<div class="plans">']
    for r in rows:
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det"><b>{r['volume']}</b> в месяц, скорость {r['speed']}. Сверх пакета — {r['over']} за 1 МБ.</div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def surf_table(rows, turbo=True):
    out = ['<div class="plans">']
    for r in rows:
        after = r["after"]
        after_txt = "после суточного лимита — без доступа до следующих суток" if after.startswith("без") else f"после лимита — {after}"
        t = " Можно докупить «Турбо»." if turbo else ""
        out.append(f"""<div class="plan">
  <div class="nm">{r['name']}</div>
  <div class="det"><b>{r['day']} в сутки</b> ({r['month']} в месяц), скорость {r['speed']}; {after_txt}.{t}</div>
  <div class="pr">{rub(r['price'])}<small>в месяц</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

def turbo_table():
    out = ['<div class="plans">']
    for n, p, d in TURBO:
        out.append(f"""<div class="plan">
  <div class="nm">{n}</div>
  <div class="det">{d}</div>
  <div class="pr">{rub(p)}<small>разово</small></div>
</div>""")
    out.append("</div>")
    return "\n".join(out)

COND_PRIVATE = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Из них 1000 ₽ сразу зачисляем на ваш баланс — фактически подключение стоит 9000 ₽.</p>
  </div>
  <div class="note">
    <h3>Оборудование</h3>
    <p>Антенну на фасад дома и Wi‑Fi роутер выдаём бесплатно на всё время, пока вы пользуетесь нашим интернетом.</p>
    <p>Если откажетесь от услуги, оборудование нужно вернуть. Если вернуть невозможно — оплатить его стоимость, 16&nbsp;500 ₽.</p>
  </div>
</div>"""

COND_BIZ_RADIO = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Это стоимость монтажа. Само оборудование — антенну и Wi‑Fi роутер — передаём в безвозмездное пользование на всё время обслуживания. При отказе от услуги оборудование нужно вернуть.</p>
  </div>
  <div class="note">
    <h3>Оплата по счёту</h3>
    <p>Для ООО и ИП действует постоплата: счёт за месяц приходит в начале следующего месяца.</p>
  </div>
</div>
<div class="callout"><p>В сёлах с тарифами «<a href="/tariff_zone2">х2</a>» и «<a href="/tariff_sputnik_biz">Спутник</a>» цену для юрлиц считаем индивидуально — она зависит от удалённости и сложности подключения.</p></div>"""

COND_BIZ_SAT = f"""<div class="cond">
  <div class="note">
    <h3>Подключение</h3>
    <div class="price-big">{rub(10000)}</div>
    <p>Это стоимость оборудования, которое мы устанавливаем. Монтаж — бесплатно.</p>
  </div>
  <div class="note">
    <h3>Оплата по счёту</h3>
    <p>Для ООО и ИП действует постоплата: счёт за месяц приходит в начале следующего месяца.</p>
  </div>
</div>"""

def apply_form(source):
    opts = "".join(f"<option>{d} район</option>" for d in DISTRICTS)
    return f"""<section class="apply" id="form">
  <div class="wrap">
    <div>
      <h2>Заявка на подключение</h2>
      <p class="muted" style="margin-top:14px">Напишите, где нужен интернет. Перезвоним, расскажем, какой тариф действует в вашем селе, и договоримся о выезде монтажников.</p>
      <p class="direct">Удобнее голосом — звоните <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
    </div>
    <form name="zayavka" method="POST" action="/spasibo" data-netlify="true" netlify-honeypot="company_site">
      <input type="hidden" name="form-name" value="zayavka">
      <input type="hidden" name="page" value="{source}">
      <p class="hp"><label>Не заполняйте <input name="company_site"></label></p>
      <div class="row2">
        <div><label for="f-name">Как к вам обращаться</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div><label for="f-tel">Телефон</label><input id="f-tel" name="phone" type="tel" autocomplete="tel" inputmode="tel" required placeholder="+7"></div>
      </div>
      <label for="f-dist">Район</label>
      <select id="f-dist" name="district"><option value="">Выберите район</option>{opts}<option>Другой</option></select>
      <label for="f-addr">Населённый пункт и адрес</label>
      <input id="f-addr" name="address" required placeholder="Например: п. Новостройка, ул. Лесная, 4">
      <label for="f-who">Кого подключаем</label>
      <select id="f-who" name="client"><option>Частный дом</option><option>Организацию (ООО, ИП)</option></select>
      <label for="f-msg">Комментарий</label>
      <textarea id="f-msg" name="message" placeholder="Необязательно"></textarea>
      <label class="consent"><input type="checkbox" name="consent" required> <span>Согласен на обработку персональных данных и с <a href="https://yadi.sk/i/C28wqz12xc28Ag" target="_blank" rel="noopener">политикой конфиденциальности</a></span></label>
      <p style="margin:18px 0 0"><button class="btn" type="submit">Отправить заявку</button></p>
    </form>
  </div>
</section>
"""

CONTACTS = f"""<section class="contacts" id="contacts">
  <div class="wrap">
    <div class="note">
      <h2 style="font-size:28px;margin-bottom:18px">Контакты</h2>
      <p><b>Телефон:</b> <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
         <b>Почта:</b> <a href="mailto:{EMAIL}">{EMAIL}</a><br>
         <b>Офис:</b> Иркутск, ул. Лермонтова, 134/1, 4 этаж</p>
      <h3 style="margin:22px 0 8px">Техподдержка</h3>
      <p>Телефон: <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
         Telegram и MAX: <a href="tel:{SUPPORT_TEL}">{SUPPORT}</a></p>
      <p class="hours">Будни 8:00–22:00, выходные 9:00–22:00 по иркутскому времени.</p>
      <div class="callout"><p>Интернет пропал сразу после полуночи? Проверьте баланс в <a href="{LK}">личном кабинете</a> — скорее всего, он закончился.</p></div>
    </div>
    <div class="note">
      <h2 style="font-size:28px;margin-bottom:18px">Документы</h2>
      <ul class="docs">
        <li><a href="https://disk.yandex.ru/i/sEdjgfnS3Bldxw" target="_blank" rel="noopener">Реквизиты ИП Малов Д.С.</a><span>PDF: ИНН, ОГРНИП, расчётный счёт, адрес</span></li>
        <li><a href="https://yadi.sk/i/uTbDkSQIcbQXaA" target="_blank" rel="noopener">Лицензия на телематические услуги связи</a><span>Скан, PDF</span></li>
        <li><a href="https://yadi.sk/i/WFzji0ZR5Bea0w" target="_blank" rel="noopener">Лицензия на услуги передачи данных</a><span>Скан, PDF</span></li>
      </ul>
      <details class="req">
        <summary>Реквизиты</summary>
        <dl>
          <dt>Полное название</dt><dd>Индивидуальный предприниматель Малов Дмитрий Сергеевич</dd>
          <dt>ОГРНИП</dt><dd>307381107900070</dd>
          <dt>ИНН</dt><dd>381100000076</dd>
          <dt>Юридический адрес</dt><dd>664023, г. Иркутск, ул. Ядринцева, д. 5, кв. 11</dd>
          <dt>Фактический адрес</dt><dd>664033, г. Иркутск, ул. Лермонтова, д. 134/1, 4 этаж</dd>
          <dt>Почтовый адрес</dt><dd>664033, г. Иркутск, а/я 4</dd>
          <dt>Банк</dt><dd>Филиал «Новосибирский» АО «АЛЬФА-БАНК», г. Новосибирск</dd>
          <dt>Расчётный счёт</dt><dd>40802810823080000518</dd>
          <dt>Корр. счёт</dt><dd>30101810600000000774</dd>
          <dt>БИК</dt><dd>045004774</dd>
        </dl>
      </details>
    </div>
  </div>
</section>
"""

FOOTER = f"""<footer>
  <div class="wrap">
    <span>© ИП Малов Д.С., «Плохая Компания», Иркутск</span>
    <span><a href="{LK}">Личный кабинет</a> &nbsp; <a href="{TG}" target="_blank" rel="noopener">Telegram</a> &nbsp; <a href="https://yandex.ru/internet/" target="_blank" rel="noopener">Проверить скорость</a> &nbsp; <a href="https://yadi.sk/i/C28wqz12xc28Ag" target="_blank" rel="noopener">Политика конфиденциальности</a></span>
  </div>
</footer>
</body>
</html>
"""

def waves_svg():
    rings = "".join(f'<circle cx="380" cy="380" r="{r}"/>' for r in range(60, 400, 52))
    pulses = "".join(f'<circle class="pulse" cx="380" cy="380" r="{r}"/>' for r in (112, 216, 320))
    return f'<svg class="waves" viewBox="0 0 760 760" aria-hidden="true">{rings}{pulses}<circle cx="380" cy="380" r="7" fill="#F2B705" stroke="none"/></svg>'

# ---------- главная ----------
def faq():
    items = [
        ("Как оставить заявку на подключение?",
         f'<p>Заполните <a href="#form">форму внизу страницы</a> или позвоните по телефону <a href="tel:{PHONE_TEL}">{PHONE}</a>. Мы перезвоним, уточним адрес и расскажем, какой тариф действует в вашем населённом пункте.</p>'),
        ("Почему такое название — «Плохая Компания»?",
         '<p class="todo">Текст ответа нужно получить от компании.</p>'),
        ("Сколько стоит подключить интернет домой?",
         '<p>Подключение стоит 10 000 ₽, из них 1000 ₽ сразу зачисляется на ваш баланс. Антенну и роутер выдаём бесплатно на всё время пользования услугой.</p>'),
        ("Какие тарифы на интернет?",
         '<p>В большинстве сёл действуют <a href="#tarif">базовые безлимитные тарифы</a> от 700 ₽ в месяц. В особо удалённых местах — тарифы <a href="/tariff_zone2">«х2»</a> или <a href="/tariff_sputnik">«Спутник»</a>. Для организаций — <a href="/tariff_biz">отдельные тарифы</a>.</p>'),
        ("Как списывается абонентская плата?",
         '<p class="todo">Текст ответа нужно получить от компании (ежедневно или раз в месяц, в какое время).</p>'),
        ("Как обстоит дело со скоростью интернета?",
         '<p>Скорость на скачивание и отдачу одинаковая и соответствует тарифу. Проверить её можно на <a href="https://yandex.ru/internet/" target="_blank" rel="noopener">yandex.ru/internet</a>. <span class="todo">Дополнить ответом компании.</span></p>'),
        ("Как оплатить интернет?",
         f'<p>Баланс и оплата — в <a href="{LK}">личном кабинете</a>. <span class="todo">Дополнить другими способами оплаты, если есть.</span></p>'),
        ("Как выбрать первый тариф?",
         '<p class="todo">Текст ответа нужно получить от компании.</p>'),
        ("Как связаться с техподдержкой?",
         f'<p>Звоните на <a href="tel:{PHONE_TEL}">{PHONE}</a> или пишите в Telegram и MAX на <a href="tel:{SUPPORT_TEL}">{SUPPORT}</a>. Работаем в будни с 8:00 до 22:00, в выходные с 9:00 до 22:00 по Иркутску.</p>'),
    ]
    out = []
    for q, a in items:
        out.append(f"<details><summary>{q}</summary><div class=\"a\">{a}</div></details>")
    return "\n".join(out)

REVIEWS = [
    ("Наталья Козловская", "Благодарю Плохую компанию, за то, что спустя долгие годы в п. Новостройка появилась мобильная связь Мегафон. Теперь мы спокойно можем позвонить нашей маме. Плохая компания — это добрые волшебники, которые вновь доказали, что они ответственные и слов на ветер не бросают. Провели интернет, а теперь ещё и мобильную связь. Не это ли сказка.... Спасибо!!!!"),
    ("Евгения Спешилова", "Тальниковское поселение, стало первопроходцем в «Плохой компании». С 2018 года, мы получаем бесперебойный, с хорошей скоростью интернет. Специалисты в компании надёжные, ответственные ребята, всегда выслушают и в кратчайшие сроки исправят проблему. В общем — МОЛОДЦЫ. Спасибо Вам за ваше доброе дело!"),
    ("Людмила Лузгина", "Уже больше года пользуемся услугами Плохой компании. Я работаю учителем, и я думаю все понимают, что значит наличие интернета для педагога. Мы участвуем в конкурсах, пользуемся электронной почтой, скачиваем презентации, просматриваем фильмы, участвуем в вебинарах и многом другом. Мне очень нравятся сами ребята из компании. Это весёлые, отзывчивые, добрые, умные люди. Им есть дело до каждого человека, а не только до какого-то отдалённо села. Они дали нам возможность быть на связи с миром. В нашем посёлке нет мобильной связи. И наличие интернета для нас настоящее окно в мир. И тем более, многие до них ХОТЕЛИ сделать связь, но никто не довёл дело до конца. А ребята из Плохой компании не только сказали, но и сделали это! И продолжают обеспечивать связью самые труднодоступные места. И оплата приемлемая и качество связи отличное. Мы благодарны их упорному труду, неиссякаемой энергии, желанию сделать нашу жизнь современной. Пусть эта компания существует долго и процветает."),
    ("Шеменкова Ольга", "Сегодня у жителей посёлка Новостройка Черемховского района праздник. У нас появилась новая услуга — сотовая связь. Посёлок находится в предгорье Восточных Саян. Ранее была проблема с электричеством — в 2010 году провели высоковольтку. Затем «Плохая компания» подключила интернет. А с сегодняшнего дня благодаря этой компании мы можем пользоваться сотовой связью. Благодарна компании, благодарна лично Дмитрию Малову. Так держать!"),
    ("Шеменкова Ольга", "«Плохая компания» появилась в моей жизни в сентябре 2019. Я теперь могу выходить в интернет и самое главное я всегда могу позвонить своим близким через вацап или вайбер. Когда необходима помощь могу позвонить односельчанам. Раньше связи не было и наш посёлок был на отшибе жизни. Спасибо вам, сотрудники «Плохая компания»."),
]

def index_page():
    dist = "".join(f"<li>{d}</li>" for d in DISTRICTS)
    rv = "".join(f"<figure><blockquote>{html.escape(t)}</blockquote><figcaption>{n}</figcaption></figure>" for n, t in REVIEWS)
    body = f"""{header('index')}
<main id="main">
<section class="hero" style="padding-top:64px">
  {waves_svg()}
  <div class="wrap">
    <div>
      <h1>Плохая <span>Компания</span></h1>
      <p class="lede">Проводим интернет в сёла и посёлки Иркутской области, куда не дотягиваются кабель и мобильная связь.</p>
      <div class="actions">
        <a class="btn" href="#form">Оставить заявку</a>
        <a class="btn ghost" href="#tarif">Посмотреть тарифы</a>
      </div>
    </div>
    <aside class="where" id="zona" aria-labelledby="zona-h">
      <h2 id="zona-h">Где мы работаем</h2>
      <p>Подключаем в населённых пунктах этих районов. Не нашли свой — всё равно оставьте заявку, проверим.</p>
      <ul>{dist}</ul>
    </aside>
  </div>
</section>

<div class="strip">
  <div class="wrap">
    <a href="{LK}"><b>Личный кабинет</b><span>Баланс и оплата услуг</span></a>
    <a href="#contacts"><b>Техподдержка</b><span>{PHONE}, Telegram и MAX</span></a>
    <a href="{TG}" target="_blank" rel="noopener"><b>Новости в Telegram</b><span>Работы на линии и объявления</span></a>
  </div>
</div>

<section id="tarif">
  <div class="wrap">
    <div class="sec-head">
      <div><h2>Тарифы</h2><p>Полный безлимит, одинаковая скорость на скачивание и отдачу.</p></div>
    </div>
    {tabs('index')}
    {unlim_table(BASE)}
    {COND_PRIVATE}
    <div class="callout"><p>В особо удалённых сёлах действуют тарифы <a href="/tariff_zone2">«х2»</a> или <a href="/tariff_sputnik">«Спутник»</a>. Перед подключением уточните у нас, какой тариф работает в вашем населённом пункте.</p></div>
  </div>
</section>

<section id="faq" style="padding-top:0">
  <div class="wrap">
    <h2 style="margin-bottom:24px">Вопросы и ответы</h2>
    <div class="faq">{faq()}</div>
  </div>
</section>

<section class="reviews" id="otzyvy">
  <div class="wrap">
    <h2>Что говорят абоненты</h2>
    <div class="rv">{rv}</div>
  </div>
</section>

{apply_form('Главная')}
{CONTACTS}
</main>
{FOOTER}"""
    title = "Плохая Компания — беспроводной интернет в сёлах Иркутской области"
    desc = "Интернет-провайдер для удалённых и небольших населённых пунктов Иркутской области. Безлимитные тарифы от 700 ₽ в месяц."
    return head(title, desc, "index") + body

def tariff_page(slug, h1, sub, content, title, form_src):
    body = f"""{header(slug)}
<main id="main">
<div class="phead"><div class="wrap"><h1>{h1}</h1><p>{sub}</p></div></div>
<section>
  <div class="wrap">
    {tabs(slug)}
    {content}
  </div>
</section>
{apply_form(form_src)}
{CONTACTS}
</main>
{FOOTER}"""
    desc = "Плохая Компания — беспроводной интернет в сёлах Иркутской области. " + sub
    return head(title, desc, slug) + body

pages = {
    "index": index_page(),
    "tariff_zone2": tariff_page(
        "tariff_zone2", "Тарифная зона «х2»",
        "Для особо удалённых сёл. Полный безлимит, скорость одинаковая в обе стороны.",
        unlim_table(X2) + COND_PRIVATE,
        "Тарифная зона «х2» — Плохая Компания", "Зона х2"),
    "tariff_sputnik": tariff_page(
        "tariff_sputnik", "Тарифная зона «Спутник»",
        "Интернет через спутник там, где нет других каналов. Тарифы с пакетом трафика на месяц или на сутки.",
        '<h3 class="plans-cap" style="margin-top:0">Пакет на месяц</h3>' + vol_table(SAT_VOL)
        + '<h3 class="plans-cap">Пакет на сутки — «Серфинг»</h3>' + surf_table(SAT_SURF)
        + '<h3 class="plans-cap">Опции «Турбо»</h3><p class="muted">Докупаются к любому тарифу, когда трафик закончился.</p>' + turbo_table()
        + COND_PRIVATE,
        "Тарифная зона «Спутник» — Плохая Компания", "Спутник"),
    "tariff_biz": tariff_page(
        "tariff_biz", "Тарифы для юрлиц",
        "Для ООО и ИП. Полный безлимит, постоплата по счёту.",
        unlim_table(BIZ) + COND_BIZ_RADIO,
        "Тарифы для юридических лиц — Плохая Компания", "Юрлица"),
    "tariff_sputnik_biz": tariff_page(
        "tariff_sputnik_biz", "«Спутник» для юрлиц",
        "Спутниковый интернет для ООО и ИП. Пакеты трафика на месяц или на сутки, постоплата по счёту.",
        '<h3 class="plans-cap" style="margin-top:0">Пакет на месяц</h3>' + vol_table(SATB_VOL)
        + '<h3 class="plans-cap">Пакет на сутки — «Серфинг»</h3>' + surf_table(SATB_SURF, turbo=False)
        + COND_BIZ_SAT,
        "Тарифная зона «Спутник» для юридических лиц — Плохая Компания", "Спутник юрлица"),
}

THANKS = head("Заявка отправлена — Плохая Компания", "Заявка на подключение отправлена.", "spasibo") + header("spasibo") + f"""
<main id="main">
<div class="phead"><div class="wrap"><h1>Заявка отправлена</h1><p>Перезвоним в рабочее время: будни 8:00–22:00, выходные 9:00–22:00 по Иркутску.</p></div></div>
<section><div class="wrap"><p>Если вопрос срочный — звоните <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p><p><a class="btn" href="/">На главную</a></p></div></section>
<span id="contacts"></span>
</main>
{FOOTER}"""

for slug, content in pages.items():
    with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(content)
with open(os.path.join(OUT, "spasibo.html"), "w", encoding="utf-8") as f:
    f.write(THANKS)
print("ok", sorted(os.listdir(OUT)))
