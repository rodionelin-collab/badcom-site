# -*- coding: utf-8 -*-
"""Генератор статического сайта badcom.ru. Запуск: python3 build.py -> папка site/"""
import os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import legal

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
.hero-logo{display:block;width:100%;max-width:640px;height:auto;color:#fff}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
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

CSS += legal.LEGAL_CSS

# ---------- шрифты: только со своего сервера ----------
import glob, shutil
FONTS_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
def font_face():
    """Берёт из папки fonts/ переменные шрифты Golos Text и Unbounded (.woff2 или .ttf).
    Если файлов нет, сайт показывает системный шрифт и ничего не грузит с чужих серверов."""
    css = ""
    fmt = {".woff2": "woff2", ".ttf": "truetype"}
    for family, key in (("Golos Text", "golos"), ("Unbounded", "unbounded")):
        found = [p for p in sorted(glob.glob(os.path.join(FONTS_SRC, "*")))
                 if key in os.path.basename(p).lower() and os.path.splitext(p)[1].lower() in fmt]
        found.sort(key=lambda p: (os.path.splitext(p)[1].lower() != ".woff2", "variable" not in p.lower()))
        if not found:
            continue
        p = found[0]
        os.makedirs(os.path.join(OUT, "fonts"), exist_ok=True)
        shutil.copy(p, os.path.join(OUT, "fonts", os.path.basename(p)))
        css += ('@font-face{font-family:"%s";src:url("/fonts/%s") format("%s");font-weight:400 900;font-style:normal;font-display:swap}\n'
                % (family, os.path.basename(p), fmt[os.path.splitext(p)[1].lower()]))
    return css
FONT_FACE = font_face()

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
<style>{FONT_FACE}{CSS}</style>
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
      <input type="hidden" name="consent_doc" value="/consent, редакция {legal.CONSENT_VERSION}">
      <input type="hidden" name="consent_time" value="">
      <label class="consent"><input type="checkbox" name="consent" required> <span>Даю <a href="/consent" target="_blank" rel="noopener">согласие на обработку персональных данных</a> для рассмотрения заявки. Ознакомлен(а) с <a href="/privacy" target="_blank" rel="noopener">Политикой обработки персональных данных</a></span></label>
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
        <li><a href="https://yadi.sk/i/uTbDkSQIcbQXaA" target="_blank" rel="noopener">Лицензия на телематические услуги связи</a><span>№ Л030-00114-77/00061756 (до 01.03.2022 — № 159794). Выдана Роскомнадзором 31.10.2017, действует до 31.10.2027. Лицензиат — ИП Малов Д.С. Территория действия: Российская Федерация. Выписка из реестра от 17.11.2026: действующая. Скан, PDF</span></li>
        <li><a href="https://yadi.sk/i/WFzji0ZR5Bea0w" target="_blank" rel="noopener">Лицензия на услуги передачи данных</a><span>№ Л030-00114-77/00073373 (до 01.03.2022 — № 177512). Выдана Роскомнадзором 02.10.2019, действует до 02.10.2029. Лицензиат — ИП Малов Д.С. Территория действия: Российская Федерация. Выписка из реестра от 17.11.2026: действующая. Скан, PDF</span></li>
        <li><a href="https://rkn.gov.ru/communication/register/license/" target="_blank" rel="noopener">Реестр лицензий в области связи</a><span>Проверить сведения о лицензиях на сайте Роскомнадзора</span></li>
        <li><a href="/privacy">Политика обработки персональных данных</a><span>Редакция от {legal.REV_DATE}</span></li>
        <li><a href="/consent">Согласие на обработку персональных данных</a><span>Для заявок с сайта</span></li>
        <li><a href="/cookies">Политика использования файлов cookie</a><span>Какие cookie использует сайт и как ими управлять</span></li>
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
          <dt>Реестр операторов ПДн</dt><dd>38-22-008580 (приказ Роскомнадзора № 156 от 30.09.2022)</dd>
        </dl>
      </details>
    </div>
  </div>
</section>
"""

FOOTER = f"""<footer>
  <div class="wrap">
    <span>© ИП Малов Д.С., «Плохая Компания», Иркутск</span>
    <span><a href="{LK}">Личный кабинет</a> &nbsp; <a href="{TG}" target="_blank" rel="noopener">Telegram</a> &nbsp; <a href="https://yandex.ru/internet/" target="_blank" rel="noopener">Проверить скорость</a></span>
    <span><a href="/privacy">Политика обработки персональных данных</a> &nbsp; <a href="/consent">Согласие на обработку ПДн</a> &nbsp; <a href="/cookies">Файлы cookie</a> &nbsp; <button class="linkbtn" type="button" data-ck-open>Настройки cookie</button></span>
  </div>
</footer>
""" + legal.COOKIE_BANNER + """</body>
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
      <h1><span class="sr">Плохая Компания</span><svg class="hero-logo" role="img" aria-label="Плохая Компания — BADCOM.RU" xmlns="http://www.w3.org/2000/svg" viewBox="14.03 122.42 254.87 38.09" fill="currentColor"><path d="M 15.800781,160.511719 L 46.988281,160.511719 C 47.964844,160.511719 48.761719,159.714844 48.761719,158.738281 L 48.761719,145.714844 C 48.761719,140.316406 48.769531,137.625 47.917969,135.03125 C 47.527344,133.839844 47.007812,132.707031 46.378906,131.648438 C 46.347656,131.59375 46.351562,131.527344 46.386719,131.476562 L 47.792969,129.648438 C 49.277344,127.710938 48.898438,124.84375 46.964844,123.359375 C 45.308594,122.089844 43.121094,122.117188 41.480469,123.378906 L 39.375,124.992188 C 39.328125,125.027344 39.265625,125.035156 39.210938,125.007812 C 36.699219,123.761719 34.199219,123.25 31.394531,123.25 C 28.59375,123.25 26.09375,123.761719 23.578125,125.007812 C 23.527344,125.035156 23.460938,125.027344 23.417969,124.992188 L 21.3125,123.378906 C 19.667969,122.117188 17.480469,122.089844 15.828125,123.359375 C 13.894531,124.84375 13.511719,127.710938 15,129.648438 L 16.402344,131.476562 C 16.441406,131.527344 16.445312,131.59375 16.414062,131.648438 C 15.78125,132.707031 15.265625,133.839844 14.875,135.03125 C 14.023438,137.625 14.03125,140.316406 14.03125,145.714844 L 14.03125,158.738281 C 14.03125,159.714844 14.828125,160.511719 15.800781,160.511719 Z M 31.394531,155.90625 C 30.902344,155.90625 30.40625,155.796875 29.949219,155.582031 L 27.066406,154.222656 C 26.253906,153.835938 25.832031,152.921875 26.074219,152.050781 L 30.070312,137.683594 C 30.257812,137.011719 30.824219,136.675781 31.394531,136.675781 C 31.964844,136.675781 32.535156,137.011719 32.722656,137.683594 L 36.714844,152.050781 C 36.957031,152.921875 36.539062,153.835938 35.722656,154.222656 L 32.84375,155.582031 C 32.382812,155.796875 31.890625,155.90625 31.394531,155.90625 Z M 41.667969,140.910156 C 41.914062,140.296875 42.046875,139.628906 42.046875,138.933594 C 42.046875,136.996094 41.019531,135.300781 39.480469,134.359375 C 39.058594,134.101562 38.566406,134.304688 38.367188,134.738281 C 38.230469,135.085938 38.355469,135.484375 38.671875,135.679688 C 39.765625,136.347656 40.496094,137.554688 40.496094,138.933594 C 40.496094,139.421875 40.40625,139.894531 40.234375,140.324219 C 40.097656,140.675781 40.226562,141.074219 40.550781,141.269531 C 40.957031,141.515625 41.492188,141.355469 41.667969,140.910156 Z M 39.667969,131.5 C 39.515625,131.875 39.6875,132.296875 40.046875,132.484375 C 42.371094,133.695312 43.957031,136.128906 43.957031,138.933594 C 43.957031,140.054688 43.703125,141.117188 43.246094,142.070312 C 43.085938,142.40625 43.1875,142.902344 43.539062,143.078125 C 43.933594,143.316406 44.441406,143.15625 44.640625,142.742188 C 45.195312,141.589844 45.503906,140.296875 45.503906,138.933594 C 45.503906,135.519531 43.566406,132.558594 40.726562,131.09375 C 40.324219,130.886719 39.835938,131.085938 39.667969,131.5 Z M 35.179688,139.792969 C 35.53125,140.410156 36.25,140.785156 37.039062,140.632812 C 37.703125,140.5 38.242188,139.96875 38.378906,139.308594 C 38.546875,138.519531 38.175781,137.796875 37.5625,137.4375 C 37.417969,137.351562 37.234375,137.378906 37.117188,137.496094 L 35.246094,139.347656 C 35.128906,139.464844 35.097656,139.648438 35.179688,139.792969 Z M 33.054688,145.105469 L 29.738281,145.105469 C 29.007812,145.105469 28.570312,145.925781 28.984375,146.527344 L 30.132812,148.222656 C 30.433594,148.667969 30.914062,148.890625 31.394531,148.890625 C 31.875,148.890625 32.355469,148.667969 32.660156,148.222656 L 33.808594,146.527344 C 34.21875,145.925781 33.785156,145.105469 33.054688,145.105469 Z M 42.109375,126.820312 C 42.941406,127.464844 43.714844,128.1875 44.414062,128.972656 C 44.550781,129.121094 44.785156,129.117188 44.910156,128.957031 L 45.644531,128 C 46.238281,127.222656 46.035156,126.0625 45.316406,125.507812 C 44.597656,124.957031 43.761719,125.042969 43.128906,125.527344 L 42.105469,126.3125 C 41.9375,126.441406 41.941406,126.691406 42.109375,126.820312 Z M 21.121094,140.910156 C 20.878906,140.296875 20.746094,139.628906 20.746094,138.933594 C 20.746094,136.996094 21.773438,135.300781 23.3125,134.359375 C 23.734375,134.101562 24.226562,134.304688 24.421875,134.738281 C 24.5625,135.085938 24.4375,135.484375 24.117188,135.679688 C 23.023438,136.347656 22.292969,137.554688 22.292969,138.933594 C 22.292969,139.421875 22.386719,139.894531 22.554688,140.324219 C 22.695312,140.675781 22.5625,141.074219 22.238281,141.269531 C 21.835938,141.515625 21.296875,141.355469 21.121094,140.910156 Z M 23.121094,131.5 C 23.273438,131.875 23.105469,132.296875 22.746094,132.484375 C 20.421875,133.695312 18.832031,136.128906 18.832031,138.933594 C 18.832031,140.054688 19.089844,141.117188 19.542969,142.070312 C 19.707031,142.40625 19.601562,142.902344 19.253906,143.078125 C 18.859375,143.316406 18.347656,143.15625 18.148438,142.742188 C 17.59375,141.589844 17.285156,140.296875 17.285156,138.933594 C 17.285156,135.519531 19.226562,132.558594 22.0625,131.09375 C 22.464844,130.886719 22.957031,131.085938 23.121094,131.5 Z M 27.609375,139.792969 C 27.257812,140.410156 26.539062,140.785156 25.753906,140.632812 C 25.089844,140.5 24.550781,139.96875 24.410156,139.308594 C 24.246094,138.519531 24.617188,137.796875 25.226562,137.4375 C 25.371094,137.351562 25.554688,137.378906 25.675781,137.496094 L 27.542969,139.347656 C 27.660156,139.464844 27.691406,139.648438 27.609375,139.792969 Z M 20.683594,126.820312 C 19.851562,127.464844 19.078125,128.1875 18.375,128.972656 C 18.242188,129.121094 18.003906,129.117188 17.882812,128.957031 L 17.148438,128 C 16.550781,127.222656 16.757812,126.0625 17.476562,125.507812 C 18.195312,124.957031 19.03125,125.042969 19.664062,125.527344 L 20.683594,126.3125 C 20.851562,126.441406 20.847656,126.691406 20.683594,126.820312" fill-rule="evenodd"/><path d="M 81.195312,137.84375 C 81.195312,138.449219 81.082031,138.945312 80.859375,139.339844 C 80.640625,139.734375 80.398438,140.042969 80.136719,140.261719 C 79.8125,140.523438 79.460938,140.726562 79.074219,140.867188 L 79.074219,141.171875 C 79.679688,141.3125 80.234375,141.554688 80.738281,141.898438 C 81.144531,142.179688 81.519531,142.570312 81.875,143.078125 C 82.226562,143.582031 82.402344,144.257812 82.402344,145.101562 L 82.402344,147.222656 C 82.402344,148.894531 81.964844,150.171875 81.085938,151.046875 C 80.210938,151.925781 78.933594,152.363281 77.261719,152.363281 L 63.042969,152.363281 C 62.4375,152.363281 62.136719,152.0625 62.136719,151.457031 L 62.136719,132.09375 C 62.136719,131.488281 62.4375,131.1875 63.042969,131.1875 L 76.050781,131.1875 C 77.726562,131.1875 79,131.625 79.878906,132.503906 C 80.753906,133.382812 81.195312,134.65625 81.195312,136.332031 Z M 68.789062,144.195312 L 68.789062,146.917969 L 74.839844,146.917969 C 75.445312,146.917969 75.75,146.617188 75.75,146.011719 L 75.75,145.101562 C 75.75,144.5 75.445312,144.195312 74.839844,144.195312 Z M 68.789062,136.632812 L 68.789062,138.75 L 73.632812,138.75 C 74.234375,138.75 74.539062,138.449219 74.539062,137.84375 L 74.539062,137.539062 C 74.539062,136.933594 74.234375,136.632812 73.632812,136.632812 Z M 99.34375,148.734375 L 92.085938,148.734375 L 91.023438,151.457031 C 90.804688,152.0625 90.398438,152.363281 89.816406,152.363281 L 84.671875,152.363281 C 84.046875,152.363281 83.84375,152.0625 84.066406,151.457031 L 91.328125,132.09375 C 91.570312,131.488281 91.972656,131.1875 92.539062,131.1875 L 98.890625,131.1875 C 99.273438,131.1875 99.550781,131.261719 99.722656,131.414062 C 99.894531,131.566406 100.019531,131.792969 100.101562,132.09375 L 107.359375,151.457031 C 107.5625,152.0625 107.359375,152.363281 106.753906,152.363281 L 101.613281,152.363281 C 101.269531,152.363281 101.011719,152.289062 100.839844,152.136719 C 100.671875,151.984375 100.523438,151.757812 100.402344,151.457031 Z M 95.5625,139.054688 L 94.050781,142.984375 L 97.378906,142.984375 L 95.863281,139.054688 Z M 130.804688,147.222656 C 130.804688,148.894531 130.367188,150.171875 129.488281,151.046875 C 128.613281,151.925781 127.335938,152.363281 125.664062,152.363281 L 110.839844,152.363281 C 110.234375,152.363281 109.933594,152.0625 109.933594,151.457031 L 109.933594,132.09375 C 109.933594,131.488281 110.234375,131.1875 110.839844,131.1875 L 125.664062,131.1875 C 127.335938,131.1875 128.613281,131.625 129.488281,132.503906 C 130.367188,133.382812 130.804688,134.65625 130.804688,136.332031 Z M 116.585938,136.933594 L 116.585938,146.617188 L 123.242188,146.617188 C 123.847656,146.617188 124.148438,146.3125 124.148438,145.707031 L 124.148438,137.84375 C 124.148438,137.238281 123.847656,136.933594 123.242188,136.933594 Z M 147.804688,146.917969 C 148.410156,146.917969 148.714844,146.617188 148.714844,146.011719 L 148.714844,145.40625 C 148.714844,144.800781 149.015625,144.5 149.621094,144.5 L 154.460938,144.5 C 155.066406,144.5 155.371094,144.800781 155.371094,145.40625 L 155.371094,147.523438 C 155.371094,149.195312 154.929688,150.472656 154.054688,151.351562 C 153.175781,152.226562 151.898438,152.667969 150.226562,152.667969 L 139.636719,152.667969 C 137.964844,152.667969 136.6875,152.226562 135.8125,151.351562 C 134.933594,150.472656 134.496094,149.195312 134.496094,147.523438 L 134.496094,136.027344 C 134.496094,134.355469 134.933594,133.078125 135.8125,132.199219 C 136.6875,131.324219 137.964844,130.886719 139.636719,130.886719 L 150.226562,130.886719 C 151.898438,130.886719 153.175781,131.324219 154.054688,132.199219 C 154.929688,133.078125 155.371094,134.355469 155.371094,136.027344 L 155.371094,138.144531 C 155.371094,138.75 155.066406,139.054688 154.460938,139.054688 L 149.621094,139.054688 C 149.015625,139.054688 148.714844,138.75 148.714844,138.144531 L 148.714844,137.539062 C 148.714844,136.933594 148.410156,136.632812 147.804688,136.632812 L 142.058594,136.632812 C 141.453125,136.632812 141.152344,136.933594 141.152344,137.539062 L 141.152344,146.011719 C 141.152344,146.617188 141.453125,146.917969 142.058594,146.917969 Z M 179.933594,147.523438 C 179.933594,149.195312 179.496094,150.472656 178.617188,151.351562 C 177.738281,152.226562 176.464844,152.667969 174.789062,152.667969 L 163.898438,152.667969 C 162.226562,152.667969 160.949219,152.226562 160.074219,151.351562 C 159.195312,150.472656 158.757812,149.195312 158.757812,147.523438 L 158.757812,136.027344 C 158.757812,134.355469 159.195312,133.078125 160.074219,132.199219 C 160.949219,131.324219 162.226562,130.886719 163.898438,130.886719 L 174.789062,130.886719 C 176.464844,130.886719 177.738281,131.324219 178.617188,132.199219 C 179.496094,133.078125 179.933594,134.355469 179.933594,136.027344 Z M 173.277344,137.539062 C 173.277344,136.933594 172.976562,136.632812 172.371094,136.632812 L 166.320312,136.632812 C 165.714844,136.632812 165.414062,136.933594 165.414062,137.539062 L 165.414062,146.011719 C 165.414062,146.617188 165.714844,146.917969 166.320312,146.917969 L 172.371094,146.917969 C 172.976562,146.917969 173.277344,146.617188 173.277344,146.011719 Z M 196.027344,152.363281 C 195.722656,152.363281 195.488281,152.289062 195.316406,152.136719 C 195.144531,151.984375 194.976562,151.757812 194.816406,151.457031 L 190.882812,142.078125 L 190.582031,142.078125 L 190.582031,151.457031 C 190.582031,152.0625 190.277344,152.363281 189.671875,152.363281 L 184.832031,152.363281 C 184.226562,152.363281 183.925781,152.0625 183.925781,151.457031 L 183.925781,132.09375 C 183.925781,131.488281 184.226562,131.1875 184.832031,131.1875 L 191.792969,131.1875 C 192.09375,131.1875 192.332031,131.261719 192.503906,131.414062 C 192.671875,131.566406 192.839844,131.792969 193,132.09375 L 197.386719,142.683594 L 197.691406,142.683594 L 202.078125,132.09375 C 202.238281,131.792969 202.40625,131.566406 202.574219,131.414062 C 202.746094,131.261719 202.984375,131.1875 203.285156,131.1875 L 210.246094,131.1875 C 210.847656,131.1875 211.152344,131.488281 211.152344,132.09375 L 211.152344,151.457031 C 211.152344,152.0625 210.847656,152.363281 210.246094,152.363281 L 205.402344,152.363281 C 204.800781,152.363281 204.496094,152.0625 204.496094,151.457031 L 204.496094,142.078125 L 204.195312,142.078125 L 200.261719,151.457031 C 200.101562,151.757812 199.933594,151.984375 199.761719,152.136719 C 199.589844,152.289062 199.355469,152.363281 199.050781,152.363281 Z M 220.589844,151.152344 C 220.589844,151.617188 220.453125,151.984375 220.179688,152.257812 C 219.910156,152.53125 219.542969,152.667969 219.078125,152.667969 L 216.355469,152.667969 C 215.890625,152.667969 215.523438,152.53125 215.25,152.257812 C 214.980469,151.984375 214.84375,151.617188 214.84375,151.152344 L 214.84375,148.734375 C 214.84375,148.269531 214.980469,147.902344 215.25,147.628906 C 215.523438,147.355469 215.890625,147.222656 216.355469,147.222656 L 219.078125,147.222656 C 219.542969,147.222656 219.910156,147.355469 220.179688,147.628906 C 220.453125,147.902344 220.589844,148.269531 220.589844,148.734375 Z M 236.984375,140.566406 C 237.328125,140.566406 237.566406,140.488281 237.695312,140.339844 C 237.828125,140.1875 237.894531,139.960938 237.894531,139.65625 L 237.894531,137.84375 C 237.894531,137.238281 237.589844,136.933594 236.984375,136.933594 L 230.9375,136.933594 L 230.9375,140.566406 Z M 230.9375,146.3125 L 230.9375,151.457031 C 230.9375,152.0625 230.632812,152.363281 230.027344,152.363281 L 225.1875,152.363281 C 224.582031,152.363281 224.28125,152.0625 224.28125,151.457031 L 224.28125,132.09375 C 224.28125,131.488281 224.582031,131.1875 225.1875,131.1875 L 239.40625,131.1875 C 241.078125,131.1875 242.355469,131.625 243.234375,132.503906 C 244.109375,133.382812 244.546875,134.65625 244.546875,136.332031 L 244.546875,141.171875 C 244.546875,142.238281 244.390625,143.089844 244.078125,143.726562 C 243.765625,144.363281 243.417969,144.851562 243.035156,145.195312 C 242.59375,145.597656 242.089844,145.871094 241.523438,146.011719 L 244.546875,151.457031 C 244.648438,151.675781 244.648438,151.882812 244.546875,152.074219 C 244.449219,152.269531 244.246094,152.363281 243.945312,152.363281 L 238.800781,152.363281 C 238.5,152.363281 238.261719,152.289062 238.089844,152.136719 C 237.917969,151.984375 237.753906,151.757812 237.589844,151.457031 L 234.867188,146.3125 Z M 253.472656,152.667969 C 251.796875,152.667969 250.523438,152.226562 249.644531,151.351562 C 248.769531,150.472656 248.328125,149.195312 248.328125,147.523438 L 248.328125,132.09375 C 248.328125,131.488281 248.632812,131.1875 249.238281,131.1875 L 254.078125,131.1875 C 254.683594,131.1875 254.984375,131.488281 254.984375,132.09375 L 254.984375,146.011719 C 254.984375,146.617188 255.289062,146.917969 255.894531,146.917969 L 261.339844,146.917969 C 261.941406,146.917969 262.246094,146.617188 262.246094,146.011719 L 262.246094,132.09375 C 262.246094,131.488281 262.546875,131.1875 263.152344,131.1875 L 267.992188,131.1875 C 268.597656,131.1875 268.902344,131.488281 268.902344,132.09375 L 268.902344,147.523438 C 268.902344,149.195312 268.460938,150.472656 267.585938,151.351562 C 266.707031,152.226562 265.433594,152.667969 263.757812,152.667969 Z M 253.472656,152.667969" fill-rule="evenodd"/></svg></h1>
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

def legal_page(slug, h1, sub, content):
    body = f"""{header(slug)}
<main id="main">
<div class="phead"><div class="wrap"><h1>{h1}</h1><p>{sub}</p></div></div>
<section><div class="wrap">{content}</div></section>
{CONTACTS}
</main>
{FOOTER}"""
    return head(h1 + " — Плохая Компания", sub, slug) + body

for slug, (h1, sub, content) in legal.build_pages(dict(PHONE=PHONE, EMAIL=EMAIL, LK=LK)).items():
    pages[slug] = legal_page(slug, h1, sub, content)

for slug, content in pages.items():
    with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(content)
with open(os.path.join(OUT, "spasibo.html"), "w", encoding="utf-8") as f:
    f.write(THANKS)
print("ok", sorted(os.listdir(OUT)))
