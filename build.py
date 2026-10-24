#!/usr/bin/env python3
"""MEYADE GAMES STUDIO static site generator.

Usage:  python build.py
Reads   _icerik/*.md  (front matter + Markdown)
Writes  index.html, blog/, about/, sitemap.xml, robots.txt, feed.xml
Needs   pip install markdown   (Pillow optional: adds width/height to body images)
"""
import datetime as dt
import html
import json
import math
import re
import shutil
import sys
from email.utils import format_datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Missing package: run  pip install markdown")

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "_icerik"
SITE = "https://meyadegamesstudio.vercel.app"
BRAND = "MEYADE GAMES STUDIO"
AUTHOR = "Mehmet Ali D."
LOGO = "/img/logo.png"
TODAY = dt.date.today()

SOCIAL = [
    ("YouTube", "https://www.youtube.com/channel/UCr0haylnBMX4Pmm43VYPXzw"),
    ("Instagram", "https://instagram.com/meyade.gamesstudio"),
    ("Facebook", "https://www.facebook.com/meyade.gamesstudio"),
]
DEV_STORE = "https://apps.apple.com/us/developer/mehmet-ali-dengis/id1875549780"

# keys: words that, found in a post slug, link that post to the game card.
GAMES = [
    dict(name="Foot Tennis Stars", icon="img/foot-tennis-stars.jpg", keys=["foot-tennis"],
         alt="Foot Tennis Stars foot tennis game icon", badge="Android coming soon",
         text="Football meets volleyball: real foot tennis rules, smash shots over the net and online matches.",
         store="https://apps.apple.com/app/apple-store/id6804052429?pt=128529947&ct=site&mt=8",
         legal=[("Privacy", "https://maliandro.github.io/futnet-stars/privacy.html"),
                ("Terms", "https://maliandro.github.io/futnet-stars/terms.html"),
                ("Support", "https://maliandro.github.io/futnet-stars/support.html")]),
    dict(name="Bolt & Breath: Last Dragon", icon="img/bolt-and-breath.jpg", keys=["bolt", "last-dragon"],
         alt="Bolt & Breath: Last Dragon dragon flying game icon",
         text="You are the last dragon. Glide over a windswept coast and burn the royal fleet that came to hunt you.",
         store="https://apps.apple.com/app/apple-store/id6804506347?pt=128529947&ct=site&mt=8",
         legal=[("Privacy", "https://maliandro.github.io/boltandbreath/privacy.html"),
                ("Terms", "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"),
                ("Support", "https://maliandro.github.io/boltandbreath/support.html")]),
    dict(name="NEO: Interactive Horror Story", icon="img/neo.jpg", keys=["neo"],
         alt="NEO interactive horror story game icon",
         text="Your friend has been missing for three days, and the campus clock stopped at 17:34. Every choice leaves a trace.",
         store="https://apps.apple.com/app/apple-store/id6790913836?pt=128529947&ct=site&mt=8",
         legal=[("Privacy", "https://maliandro.github.io/neo/en/privacy.html"),
                ("Terms", "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"),
                ("Support", "https://maliandro.github.io/neo/en/support.html")]),
    dict(name="Protokol-Ø: AI Thriller Story", icon="img/protokol-0.jpg", keys=["protokol", "protocol"],
         alt="Protokol-Ø AI thriller story game icon",
         text="An AI thriller told through cases: approve, reject, escalate, and find out who your decisions reach.",
         store="https://apps.apple.com/app/apple-store/id6761679315?pt=128529947&ct=site&mt=8",
         legal=[("Privacy", "https://sites.google.com/view/protokolzero/privacy-policy"),
                ("Terms", "https://sites.google.com/view/protokolzero/terms-of-service"),
                ("Support", "https://sites.google.com/view/protokolzero")]),
    dict(name="Tomb Maze: Horror Escape", icon="img/tomb-maze.jpg", keys=["tomb-maze", "tomb"],
         alt="Tomb Maze: Horror Escape horror maze game icon",
         text="Escape the mazes beneath a collapsing pyramid, with Guardians that see and hear you.",
         store="https://apps.apple.com/app/apple-store/id6819377082?pt=128529947&ct=site&mt=8", site="https://maliandro.github.io/tomb-maze-site/",
         legal=[("Privacy", "https://maliandro.github.io/tomb-maze-site/privacy.html"),
                ("Terms", "https://maliandro.github.io/tomb-maze-site/terms.html"),
                ("Support", "https://maliandro.github.io/tomb-maze-site/support.html")]),
    dict(name="Prof. Nano", icon="img/prof-nano.jpg", keys=["prof-nano", "nano"],
         alt="Prof. Nano science game for kids icon",
         text="A game that sparks kids' curiosity about science.", note="Turkish now · English coming soon",
         store="https://apps.apple.com/app/apple-store/id6800853916?pt=128529947&ct=site&mt=8", site="https://maliandro.github.io/profnano-site/",
         legal=[("Website", "https://maliandro.github.io/profnano-site/"),
                ("Privacy", "https://maliandro.github.io/profnano-site/privacy.html"),
                ("Terms", "https://maliandro.github.io/profnano-site/kosullar.html"),
                ("Support", "https://maliandro.github.io/profnano-site/")]),
]
APPS = [
    dict(name="Unutma", icon="img/unutma.jpg", keys=["unutma"],
         alt="Unutma offline personal assistant app icon", platforms="iOS, Android",
         play="https://play.google.com/store/apps/details?id=com.mehmet.unutma",
         text="A private personal assistant that works offline: say it, and it keeps your reminders, notes and expenses.",
         store="https://apps.apple.com/app/apple-store/id6758889495?pt=128529947&ct=site&mt=8",
         legal=[("Website", "https://unutma-blog.vercel.app/"), ("Privacy", "https://unutma-blog.vercel.app/privacy"),
                ("Terms", "https://unutma-blog.vercel.app/terms"), ("Support", "https://unutma-blog.vercel.app/")]),
    dict(name="Mobies", icon="img/mobies.jpg", keys=["mobies"],
         alt="Mobies customer book app icon",
         text="A customer book for small businesses: know your regulars, with no account and your data on your phone.",
         store="https://apps.apple.com/app/apple-store/id6766030370?pt=128529947&ct=site&mt=8",
         legal=[("Website", "https://mobies.vercel.app/"), ("Privacy", "https://mobies.vercel.app/privacy.html"),
                ("Terms", "https://mobies.vercel.app/terms.html"), ("Support", "https://mobies.vercel.app/")]),
]

e = lambda s: html.escape(str(s), quote=True)

# Each post links to 1-2 related posts ("Related" line under the article).
RELATED = {
    "neo": ["protokol-zero", "tomb-maze"],
    "protokol-zero": ["neo", "tomb-maze"],
    "tomb-maze": ["neo", "protokol-zero"],
    "unutma": ["mobies"],
    "mobies": ["unutma"],
    "bolt-and-breath": ["foot-tennis-stars", "prof-nano"],
    "foot-tennis-stars": ["bolt-and-breath", "prof-nano"],
    "prof-nano": ["bolt-and-breath", "foot-tennis-stars"],
}


def alt_for(src, fallback=""):
    """Descriptive alt text for a site image (game/app icons, logo)."""
    s = (src or "").lstrip("/")
    for it in GAMES + APPS:
        if it["icon"] == s:
            return it.get("alt") or f"{it['name']} icon"
    if "logo" in s:
        return f"{BRAND} logo"
    return fallback


# ---------------------------------------------------------------- content
def parse_front_matter(text):
    meta, body = {}, text
    m = re.match(r"^﻿?---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return meta, body
    head, body = m.group(1), m.group(2)
    key = None
    for line in head.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s*-\s+(.*)$", line)
        if item and key:  # YAML list item
            meta.setdefault(key, [])
            if isinstance(meta[key], list):
                meta[key].append(unquote(item.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if kv:
            key, val = kv.group(1).lower(), kv.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                meta[key] = [unquote(v) for v in val[1:-1].split(",") if v.strip()]
            else:
                meta[key] = unquote(val) if val else []
    return meta, body


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def parse_date(v, fallback):
    try:
        return dt.date.fromisoformat(str(v).strip()[:10])
    except ValueError:
        return fallback


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "post"


def local_img(path):
    """Return root-absolute site path for a local image, or None."""
    if not path:
        return None
    if re.match(r"^https?://", path):
        return path
    p = path.lstrip("/")
    return "/" + p if (ROOT / p).is_file() else None


def img_size(site_path):
    try:
        from PIL import Image
        with Image.open(ROOT / site_path.lstrip("/")) as im:
            return im.size
    except Exception:
        return None


def enhance_images(body_html):
    def fix(m):
        tag = m.group(0)
        if "loading=" not in tag:
            tag = tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
        src = re.search(r'src="([^"]+)"', tag)
        if src and "width=" not in tag and not src.group(1).startswith("http"):
            size = img_size(src.group(1))
            if size:
                tag = tag.replace("<img ", f'<img width="{size[0]}" height="{size[1]}" ', 1)
        return tag
    return re.sub(r"<img [^>]*>", fix, body_html)


def brandcase(text):
    """The studio name is always written in capitals."""
    return re.sub(r"(?i)\bmeyade\s+games\s+studio\b", BRAND, text)


def load_posts():
    posts = []
    for f in sorted(CONTENT.glob("*.md")):
        meta, body = parse_front_matter(brandcase(f.read_text(encoding="utf-8")))
        mtime = dt.date.fromtimestamp(f.stat().st_mtime)
        title = meta.get("title") or f.stem
        lines = body.lstrip().splitlines()
        if lines and re.match(r"^#\s", lines[0]):  # drop duplicate H1
            body = "\n".join(lines[1:])
        # bare URLs -> clickable links (skips Markdown links, autolinks and HTML attributes)
        body = re.sub(r'(?<![(<"\'=\]])\b(https?://[^\s<>()\]]+?)(?=[.,;:!?]?(?:\s|$))', r"<\1>", body)
        words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", body)))
        kw = meta.get("keywords") or []
        if isinstance(kw, str):
            kw = [k.strip() for k in kw.split(",") if k.strip()]
        try:
            order = float(meta.get("order"))
        except (TypeError, ValueError):
            order = None
        p = dict(
            file=f.name, title=title, seo_title=meta.get("seo_title") if isinstance(meta.get("seo_title"), str) else "", slug=slugify(meta.get("slug") or f.stem),
            description=meta.get("description") or "", keywords=kw,
            date=parse_date(meta.get("date", ""), mtime), order=order,
            updated=parse_date(meta.get("updated", ""), None) if meta.get("updated") else None,
            cover=local_img(meta.get("cover") if isinstance(meta.get("cover"), str) else None),
            cta_label=meta.get("cta_label") or "", cta_url=meta.get("cta_url") or "",
            cta2_label=meta.get("cta2_label") or "", cta2_url=meta.get("cta2_url") or "",
            cta3_label=meta.get("cta3_label") or "", cta3_url=meta.get("cta3_url") or "",
            game=meta.get("game") if isinstance(meta.get("game"), str) else "",
            minutes=max(1, math.ceil(words / 220)),
            html=enhance_images(markdown.markdown(body, extensions=["extra", "sane_lists"])),
        )
        p["modified"] = p["updated"] or p["date"]
        if p["cover"] is None and meta.get("cover"):
            print(f"  ! {f.name}: cover not found: {meta.get('cover')}")
        posts.append(p)
    slugs = [p["slug"] for p in posts]
    for s in set(slugs):
        if slugs.count(s) > 1:
            sys.exit(f"Duplicate slug: {s}")
    return posts


def sort_posts(posts):
    # 'order' first (ascending), posts without order after them, newest first.
    return sorted(posts, key=lambda p: (p["order"] is None, p["order"] or 0, -p["date"].toordinal()))


def url_of(p):
    return "/about/" if p["slug"] == "about" else f"/blog/{p['slug']}/"


def fmt_date(d):
    return f"{d.strftime('%b')} {d.day}, {d.year}"


# ---------------------------------------------------------------- logo mark
def mark_svg(uid, cls="mark"):
    cells = [(0, r) for r in range(5)] + [(1, 1), (2, 2), (3, 1)] + [(4, r) for r in range(5)]
    m = "".join(f'<rect x="{123 + c * 54}" y="{123 + r * 54}" width="50" height="50" rx="9"/>' for c, r in cells)
    ring = []
    arcs = [(170, 300, 18, 13), (-30, 120, 14, 24)]  # start, end, edge size, peak size (matches the logo)
    for a0, a1, s_edge, s_peak in arcs:
        n = (a1 - a0) // 10 + 1
        for i in range(n):
            t = i / (n - 1)
            if s_peak > s_edge:
                s = s_edge + (s_peak - s_edge) * math.sin(math.pi * t)
            else:
                s = s_edge - (s_edge - s_peak) * max(0.0, (t - .6) / .4)
            ang = math.radians(a0 + i * 10)
            x, y = 256 + 220 * math.cos(ang), 256 + 220 * math.sin(ang)
            ring.append(f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s * .25:.1f}"/>')
    return (
        f'<svg class="{cls}" viewBox="0 0 512 512" aria-hidden="true" focusable="false">'
        f'<defs><linearGradient id="gm{uid}" x1="120" y1="0" x2="392" y2="0" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="#36bfcd"/><stop offset="1" stop-color="#6c6ae8"/></linearGradient>'
        f'<linearGradient id="gr{uid}" x1="30" y1="0" x2="482" y2="0" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="#6fb7ab"/><stop offset="1" stop-color="#7458f2"/></linearGradient></defs>'
        f'<g class="ring" fill="url(#gr{uid})">{"".join(ring)}</g>'
        f'<g fill="url(#gm{uid})">{m}</g></svg>'
    )


# ---------------------------------------------------------------- layout
def jsonld(obj):
    # yapısal veride kanonik App Store adresi; kampanya (pt/ct) yalnız tıklanan düğmelerde
    metin = re.sub(r"https://apps\.apple\.com/app/apple-store/id(\d+)\?pt=\d+&ct=[\w-]+&mt=8",
                   r"https://apps.apple.com/app/id\1", json.dumps(obj, ensure_ascii=False))
    return '<script type="application/ld+json">' + metin.replace("</", "<\\/") + "</script>"


ORG = {
    "@type": "Organization", "@id": SITE + "/#org", "name": BRAND, "url": SITE + "/",
    "logo": {"@type": "ImageObject", "url": SITE + LOGO, "width": 600, "height": 600},
    "sameAs": [u for _, u in SOCIAL], "founder": {"@type": "Person", "name": AUTHOR},
}

SCRIPT = """<script>
(function(){
  var els=document.querySelectorAll('.reveal');
  var still=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!('IntersectionObserver' in window)||still){els.forEach(function(el){el.classList.add('in')});}
  else{var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{rootMargin:'0px 0px -6% 0px'});
    els.forEach(function(el){io.observe(el)});}
  document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){
    var done=function(){b.textContent='Link copied';setTimeout(function(){b.textContent='Copy link'},2000)};
    if(navigator.clipboard){navigator.clipboard.writeText(b.dataset.copy).then(done,function(){prompt('Copy this link:',b.dataset.copy)});}
    else{prompt('Copy this link:',b.dataset.copy);}
  });});
  // ?k=ig / ?k=yt: bio'dan gelen ziyaretçinin App Store düğmeleri o kanalın ct koduyla açılır (sayım Apple'da; burada veri tutulmaz)
  var KANAL={ig:'ig-bio',yt:'yt-bio'},k=null;
  try{k=new URLSearchParams(location.search).get('k')||sessionStorage.getItem('k');if(KANAL[k])sessionStorage.setItem('k',k);}catch(_){}
  if(KANAL[k])document.querySelectorAll('a[href*="apps.apple.com/app/apple-store/"]').forEach(function(a){a.href=a.href.replace(/ct=[\\w-]+/,'ct='+KANAL[k]);});
})();
</script>"""


def page(*, path, title, desc, body, active, image=None, og_type="website", ld=(), head_extra="",
         robots="index, follow, max-image-preview:large"):
    canonical = SITE + path
    img = image or LOGO
    img_abs = img if img.startswith("http") else SITE + img
    nav = "".join(
        f'<a href="{href}"{CUR if key == active else ""}>{label}</a>'
        for key, href, label in [("home", "/", "Home"), ("games", "/#games", "Games"),
                                 ("blog", "/blog/", "Blog"), ("about", ABOUT_HREF, "About")])
    lds = "\n".join(jsonld(x) for x in ld)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0a0e17">
<meta name="author" content="{e(AUTHOR)}">
<meta name="robots" content="{robots}">
{head_extra}<meta property="og:site_name" content="{BRAND}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{e(img_abs)}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{e(img_abs)}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" title="{BRAND} blog" href="/feed.xml">
<link rel="stylesheet" href="/style.css">
<script>document.documentElement.classList.add('js')</script>
{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="/" aria-label="{BRAND} home">{mark_svg("n", "mark mark-sm")}<span>{BRAND}</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
{body}
<footer class="site-foot">
  <div class="wrap">
    <nav class="foot-links" aria-label="Footer"><a href="/">Home</a><a href="/blog/">Blog</a><a href="{ABOUT_HREF}">About</a><a href="/feed.xml">RSS</a>{"".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)}</nav>
    <p>© {TODAY.year} {e(AUTHOR)} · {BRAND}</p>
  </div>
</footer>
{SCRIPT}
</body>
</html>
"""


def write(rel, text):
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")


def cover_img(p, size, cls="cover"):
    src = p["cover"] or "/img/logo-mark.png"
    return f'<img class="{cls}" src="{e(src)}" alt="{e(alt_for(src, p["title"]))}" width="{size}" height="{size}" loading="lazy" decoding="async">'


def post_card(p, heading="h3"):
    return f"""<li class="post-card reveal">
  <a href="{url_of(p)}">
    {cover_img(p, 64)}
    <span class="pc-body">
      <{heading} class="pc-title">{e(p["title"])}</{heading}>
      <span class="pc-desc">{e(p["description"])}</span>
      <span class="pc-meta"><time datetime="{p["date"].isoformat()}">{fmt_date(p["date"])}</time> · {p["minutes"]} min read</span>
    </span>
  </a>
</li>"""


# ---------------------------------------------------------------- pages
def game_story(item, posts):
    if item.get("story"):
        return item["story"]
    for p in posts:  # explicit 'game:' field wins
        if p["game"] and slugify(p["game"]) in (slugify(k) for k in item["keys"] + [item["name"]]):
            return p
    for p in posts:  # same cover image as the card
        if p["cover"] == "/" + item["icon"]:
            return p
    for p in posts:
        if any(f"-{k}-" in f"-{p['slug']}-" for k in item["keys"]):
            return p
    return None


def item_card(item, posts, size):
    story = game_story(item, posts)
    lang = f' hreflang="{item["lang"]}"' if item.get("lang") else ""
    store = (f'<a class="store" href="{item["store"]}" target="_blank" rel="noopener">App Store</a>'
             if item.get("store") else '<span class="store soon">Coming soon</span>')
    if item.get("play"):
        store += f'<a class="store" href="{item["play"]}" target="_blank" rel="noopener">Google Play</a>'
    if item.get("badge"):
        store += f'<span class="store soon">{e(item["badge"])}</span>'
    story_link = f'<a class="story" href="{url_of(story)}">Read the story</a>' if story else ""
    note = f'<p class="note">{e(item["note"])}</p>' if item.get("note") else ""
    legal = "".join(f'<a href="{u}"{lang}>{n}</a>' for n, u in item["legal"])
    return f"""<li class="card reveal">
        <img src="/{item["icon"]}" alt="{e(item.get("alt") or item["name"] + " icon")}" width="{size}" height="{size}" loading="lazy" decoding="async">
        <div class="body">
          <h3>{e(item["name"])}</h3>
          <p>{e(item["text"])}</p>
          {note}<div class="actions">{store}{story_link}</div>
          <p class="legal">{legal}</p>
        </div>
      </li>"""


def particles():
    spots = [(6, 11, -2, 6), (14, 15, -9, 4), (23, 12, -5, 8), (31, 17, -12, 5), (42, 13, -3, 7), (51, 19, -14, 4),
             (60, 12, -7, 6), (68, 16, -1, 9), (77, 14, -10, 5), (85, 18, -6, 7), (93, 13, -11, 4), (37, 21, -16, 5)]
    return '<div class="particles" aria-hidden="true">' + "".join(
        f'<i style="--x:{x}%;--d:{d}s;--w:{w}s;--s:{s}px"></i>' for x, d, w, s in spots) + "</div>"


def build_home(posts, blog_posts):
    gsc = ROOT / "_gsc.txt"
    verify = "<!-- google-site-verification -->\n"
    if gsc.is_file() and gsc.read_text(encoding="utf-8").strip():
        token = gsc.read_text(encoding="utf-8").strip()
        token = re.sub(r'.*content="([^"]+)".*', r"\1", token, flags=re.S)  # accept full meta tag too
        verify = f'<meta name="google-site-verification" content="{e(token)}">\n'

    items = []
    for i, g in enumerate(GAMES + APPS, 1):
        is_game = g in GAMES
        obj = {"@type": ["VideoGame", "MobileApplication"] if is_game else "MobileApplication",
               "name": g["name"], "operatingSystem": g.get("platforms", "iOS"),
               "applicationCategory": "GameApplication" if is_game else "UtilitiesApplication",
               "image": SITE + "/" + g["icon"], "description": g["text"], "author": {"@id": SITE + "/#org"}}
        if g.get("store") or g.get("site"):
            obj["url"] = g.get("store") or g.get("site")
        if g.get("play"):
            obj["sameAs"] = [u for u in (g.get("store"), g["play"]) if u]
        if is_game:
            obj["gamePlatform"] = "iOS"
        items.append({"@type": "ListItem", "position": i, "item": obj})
    ld = [
        {"@context": "https://schema.org", **ORG},
        {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": BRAND,
         "url": SITE + "/", "inLanguage": "en", "publisher": {"@id": SITE + "/#org"}},
        {"@context": "https://schema.org", "@type": "ItemList", "name": f"Games and apps by {BRAND}",
         "itemListElement": items},
    ]
    latest = blog_posts[:3]
    blog_section = ""
    if latest:
        blog_section = f"""
  <section id="blog" class="wrap section" aria-labelledby="blog-h">
    <h2 id="blog-h">From the blog</h2>
    <ul class="post-list">
{chr(10).join(post_card(p) for p in latest)}
    </ul>
    <p class="more-link"><a class="btn" href="/blog/">All stories</a></p>
  </section>"""

    body = f"""<div class="hero">
  {particles()}
  <div class="wrap hero-in">
    {mark_svg("h", "mark mark-lg")}
    <h1>{BRAND}</h1>
    <p class="lead">Indie games made by one developer in Turkey</p>
    <span class="arrow" aria-hidden="true"></span>
    <nav class="cta" aria-label="Quick links">
      <a class="btn primary" href="{DEV_STORE}" target="_blank" rel="noopener">All games on the App Store</a>
      <a class="btn" href="/blog/">Read the blog</a>
    </nav>
  </div>
</div>

<main id="main">
  <section id="journey" class="wrap section reveal" aria-labelledby="journey-h">
    <h2 id="journey-h">My journey</h2>
    <p>Hi, I'm Mehmet Ali, the developer behind {BRAND}. My journey started with <strong>Unutma</strong>, a private personal assistant app I built because I kept forgetting things. Building it taught me how to make apps; publishing taught me everything else.</p>
    <ol class="timeline">
      <li><span class="when">Feb 2026</span><span class="what"><strong>Unutma</strong> — the app that started it all</span></li>
      <li><span class="when">Apr 2026</span><span class="what"><strong>Protokol-Ø</strong> — my first game, an AI thriller story</span></li>
      <li><span class="when">Jul 2026</span><span class="what"><strong>NEO</strong> — an interactive horror story where the wrong door kills you</span></li>
      <li><span class="when">Jul 2026</span><span class="what"><strong>Mobies</strong> — a customer book for small businesses</span></li>
      <li><span class="when">Sep 2026</span><span class="what"><strong>Foot Tennis Stars</strong> and <strong>Bolt &amp; Breath</strong></span></li>
      <li><span class="when">Oct 2026</span><span class="what"><strong>Tomb Maze</strong> and <strong>Prof. Nano</strong>, both out on the same day</span></li>
      <li><span class="when">Next</span><span class="what"><strong>Prof. Nano</strong> in English, and Android</span></li>
    </ol>
    <p>Every day I post a short clip: gameplay, behind the scenes and what I'm building next. Most of my games are free on the App Store.</p>
  </section>

  <section id="games" class="wrap section" aria-labelledby="games-h">
    <h2 id="games-h">Games</h2>
    <ul class="cards">
      {"".join(item_card(g, posts, 72) for g in GAMES)}
    </ul>
  </section>

  <section id="apps" class="wrap section" aria-labelledby="apps-h">
    <h2 id="apps-h">Apps</h2>
    <ul class="cards small">
      {"".join(item_card(a, posts, 56) for a in APPS)}
    </ul>
  </section>
{blog_section}

  <section id="follow" class="wrap section reveal" aria-labelledby="follow-h">
    <h2 id="follow-h">Follow the journey</h2>
    <p>A new clip every day.</p>
    <nav class="social" aria-label="Social links">
      {"".join(f'<a class="btn" href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)}
      <a class="btn" href="{DEV_STORE}" target="_blank" rel="noopener">App Store</a>
    </nav>
    <p class="contact">Contact: <a href="mailto:mealidengis@gmail.com">mealidengis@gmail.com</a></p>
  </section>
</main>"""
    html_out = page(path="/", title=f"{BRAND} — Indie games by one developer in Turkey",
                    desc=f"{BRAND}: indie mobile games and apps by one developer in Turkey. NEO, Bolt & Breath, Foot Tennis Stars, Protokol-Ø and the stories behind them.",
                    body=body, active="home", ld=ld, head_extra=verify)
    write("index.html", html_out)


def build_blog_index(blog_posts):
    cards = "\n".join(post_card(p, "h2") for p in blog_posts) or "<li>No stories yet.</li>"
    body = f"""<main id="main" class="wrap section page-top">
  <header class="page-head">
    <h1>Blog</h1>
    <p class="lead-left">Stories behind the games: how they started, what went wrong and what I learned making them.</p>
  </header>
  <ul class="post-list">
{cards}
  </ul>
</main>"""
    ld = [{"@context": "https://schema.org", "@type": "Blog", "name": f"{BRAND} blog", "url": SITE + "/blog/",
           "inLanguage": "en", "publisher": {"@id": SITE + "/#org"},
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": SITE + url_of(p),
                         "datePublished": p["date"].isoformat()} for p in blog_posts]}]
    write("blog/index.html", page(path="/blog/", title=f"Blog — {BRAND}",
                                  desc=f"Stories behind the indie games of {BRAND}: development notes, launches and lessons from one developer in Turkey.",
                                  body=body, active="blog", ld=ld))


def seo_title(p):
    """<title>: front-matter seo_title (keyword first); brand appended only if it stays <= 60 chars."""
    t = p.get("seo_title") or p["title"]
    if BRAND in t:
        return t
    full = f"{t} — {BRAND}"
    return full if len(full) <= 60 or not p.get("seo_title") else t


def share_links(p):
    from urllib.parse import quote
    u = SITE + url_of(p)
    x = f"https://x.com/intent/post?url={quote(u, safe='')}&text={quote(p['title'], safe='')}"
    fb = f"https://www.facebook.com/sharer/sharer.php?u={quote(u, safe='')}"
    return (f'<div class="share"><span>Share</span><a href="{e(x)}" target="_blank" rel="noopener">X</a>'
            f'<a href="{e(fb)}" target="_blank" rel="noopener">Facebook</a>'
            f'<button type="button" data-copy="{e(u)}">Copy link</button></div>')


def build_post(p, prev_p, next_p, by_slug=None):
    is_about = p["slug"] == "about"
    cta = ""
    butonlar = []
    for i, (lk, uk) in enumerate([("cta_label", "cta_url"), ("cta2_label", "cta2_url"), ("cta3_label", "cta3_url")]):
        if p.get(lk) and p.get(uk):
            ext = ' target="_blank" rel="noopener"' if p[uk].startswith("http") else ""
            butonlar.append(f'<a class="btn{" primary" if i == 0 else ""}" href="{e(p[uk])}"{ext}>{e(p[lk])}</a>')
    if butonlar:
        cta = '<p class="post-cta">' + " ".join(butonlar) + "</p>"
    more = ""
    if not is_about and (prev_p or next_p):
        links = ""
        if prev_p:
            links += f'<a class="more-card prev" href="{url_of(prev_p)}"><span class="dir">Previous</span>{cover_img(prev_p, 48, "mini")}<span class="t">{e(prev_p["title"])}</span></a>'
        if next_p:
            links += f'<a class="more-card next" href="{url_of(next_p)}"><span class="dir">Next</span>{cover_img(next_p, 48, "mini")}<span class="t">{e(next_p["title"])}</span></a>'
        more = f'<nav class="more-stories" aria-labelledby="more-h"><h2 id="more-h">More stories</h2><div class="more-grid">{links}</div></nav>'
    related = ""
    rel = [by_slug[s_] for s_ in RELATED.get(p["slug"], []) if by_slug and s_ in by_slug]
    if rel and not is_about:
        related = ('<p class="related"><span>Related:</span> '
                   + " · ".join(f'<a href="{url_of(r)}">{e(r["title"])}</a>' for r in rel) + "</p>")
    meta = "" if is_about else (f'<p class="post-meta"><time datetime="{p["date"].isoformat()}">{fmt_date(p["date"])}</time>'
                                f' · {p["minutes"]} min read · {e(AUTHOR)}</p>')
    crumb = "" if is_about else '<p class="crumb"><a href="/blog/">Blog</a></p>'
    cover = (f'<img class="post-cover" src="{e(p["cover"])}" alt="{e(alt_for(p["cover"], p["title"]))}" width="96" height="96" decoding="async" fetchpriority="high">'
             if p["cover"] else mark_svg("c", "mark post-cover"))
    body = f"""<main id="main" class="post-wrap page-top">
  <article class="post">
    <header class="post-head">
      {cover}
      {crumb}
      <h1>{e(p["title"])}</h1>
      {meta}
    </header>
    <div class="prose">
{p["html"]}
    </div>
    {cta}
    {related}
    {"" if is_about else share_links(p)}
  </article>
  {more}
</main>"""
    img = p["cover"] or LOGO
    img_abs = img if img.startswith("http") else SITE + img
    if is_about:
        ld = [{"@context": "https://schema.org", "@type": "ProfilePage", "url": SITE + "/about/",
               "mainEntity": {"@type": "Person", "@id": SITE + "/about/#person", "name": AUTHOR,
                              "alternateName": "Mehmet Ali", "jobTitle": "Indie game developer",
                              "url": SITE + "/about/", "worksFor": {"@id": SITE + "/#org"},
                              "homeLocation": {"@type": "Country", "name": "Turkey"}}},
              {"@context": "https://schema.org", **ORG}]
        title = seo_title(p)
        path, active, og = "/about/", "about", "profile"
    else:
        ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
               "description": p["description"], "image": img_abs, "url": SITE + url_of(p),
               "mainEntityOfPage": SITE + url_of(p), "datePublished": p["date"].isoformat(),
               "dateModified": p["modified"].isoformat(), "inLanguage": "en",
               "keywords": ", ".join(p["keywords"]) or None, "wordCount": None,
               "author": {"@type": "Person", "name": AUTHOR, "url": SITE + ABOUT_HREF},
               "publisher": {"@type": "Organization", "name": BRAND, "url": SITE + "/",
                             "logo": {"@type": "ImageObject", "url": SITE + LOGO}}}]
        ld[0] = {k: v for k, v in ld[0].items() if v is not None}
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": SITE + url_of(p)}]})
        title = seo_title(p)
        path, active, og = url_of(p), "blog", "article"
    extra = ""
    if p["keywords"]:
        extra += f'<meta name="keywords" content="{e(", ".join(p["keywords"]))}">\n'
    if not is_about:
        extra += (f'<meta property="article:published_time" content="{p["date"].isoformat()}">\n'
                  f'<meta property="article:modified_time" content="{p["modified"].isoformat()}">\n'
                  f'<meta property="article:author" content="{e(AUTHOR)}">\n')
    write(path.strip("/") + "/index.html",
          page(path=path, title=title, desc=p["description"] or p["title"], body=body, active=active,
               image=p["cover"], og_type=og, ld=ld, head_extra=extra))


def build_404():
    body = ('<main id="main" class="wrap section page-top">\n  <header class="page-head">\n'
            '    <h1>Page not found</h1>\n'
            '    <p class="lead-left">This page doesn\'t exist or has moved. Try the <a href="/">home page</a>, '
            'the <a href="/blog/">blog</a> or the <a href="/#games">games</a>.</p>\n  </header>\n</main>')
    write("404.html", page(path="/404.html", title=f"Page not found — {BRAND}", desc=f"Page not found on {BRAND}.",
                           body=body, active="", robots="noindex"))


DEFAULT_ABOUT = dict(
    file="(built-in)", slug="about", title="About", description=f"Mehmet Ali, the one developer behind {BRAND}.",
    keywords=[], cover=None, cta_label="See my games on the App Store", cta_url=DEV_STORE, cta2_label="", cta2_url="", cta3_label="", cta3_url="", game="", minutes=1,
    date=TODAY, modified=TODAY, order=None, updated=None,
    html=f"<p>Hi, I'm Mehmet Ali, the developer behind {BRAND}. I make small mobile games and apps on my own in Turkey, "
         "and I share every step of the way with a short clip each day.</p>",
)


def build_feed(blog_posts):
    items = []
    for p in blog_posts[:30]:
        when = dt.datetime.combine(p["date"], dt.time(9, 0), tzinfo=dt.timezone.utc)
        items.append(f"""  <item>
    <title>{e(p["title"])}</title>
    <link>{SITE}{url_of(p)}</link>
    <guid isPermaLink="true">{SITE}{url_of(p)}</guid>
    <pubDate>{format_datetime(when)}</pubDate>
    <description>{e(p["description"])}</description>
  </item>""")
    last = max([p["modified"] for p in blog_posts], default=TODAY)
    write("feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/feed.xsl"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{BRAND} blog</title>
  <link>{SITE}/blog/</link>
  <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Stories behind the indie games of {BRAND}.</description>
  <language>en</language>
  <lastBuildDate>{format_datetime(dt.datetime.combine(last, dt.time(9, 0), tzinfo=dt.timezone.utc))}</lastBuildDate>
{chr(10).join(items)}
</channel>
</rss>
""")


def build_sitemap(all_posts, blog_posts):
    last = max([p["modified"] for p in blog_posts], default=TODAY)
    urls = [("/", last), ("/blog/", last)] + [(url_of(p), p["modified"]) for p in all_posts]
    body = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{d.isoformat()}</lastmod></url>" for u, d in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n'
                         f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    return [u for u, _ in urls]


ABOUT_HREF = "/about/"
CUR = ' aria-current="page"'


def main():
    CONTENT.mkdir(exist_ok=True)
    posts = sort_posts(load_posts())
    about = next((p for p in posts if p["slug"] == "about"), None) or DEFAULT_ABOUT
    blog_posts = [p for p in posts if p["slug"] != "about"]
    for d in ("blog", "about"):  # generated folders: rebuild from scratch
        shutil.rmtree(ROOT / d, ignore_errors=True)
    build_home(blog_posts, blog_posts)
    build_blog_index(blog_posts)
    for i, p in enumerate(blog_posts):
        build_post(p, blog_posts[i - 1] if i > 0 else None, blog_posts[i + 1] if i + 1 < len(blog_posts) else None,
                   {q["slug"]: q for q in blog_posts})
    build_post(about, None, None)
    build_404()
    build_feed(blog_posts)
    urls = build_sitemap(blog_posts + [about], blog_posts)
    print(f"Built {len(blog_posts)} posts + about ({about['file']}) -> {len(urls)} URLs in sitemap")
    for p in blog_posts:
        print(f"  {url_of(p):45} {p['date']}  {p['minutes']} min  ({p['file']})")


if __name__ == "__main__":
    main()
