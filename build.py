#!/usr/bin/env python3
"""
Static site builder for mostyngriffith.com (GitHub Pages).

  python3 build.py

Reads content/*.md, writes index.html, work/<slug>/index.html and 404.html.
No third-party packages needed.

Assets: content refers to images as  CDN/<filename>.  If the file exists in
./assets/ (run scripts/fetch_assets.py once to download them) the local copy
is used; otherwise the page links to the original Webflow CDN URL.
"""
import html
import json
import os
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
CDN_BASE = "https://cdn.prod.website-files.com/68d9d5fedda8c841de1ca7fb/"
CDN_VIDEO_BASE = "https://cdn.prod.website-files.com/68d9d5fedda8c841de1ca7fb%2F"

SITE = {
    "name": "Mostyn Griffith",
    "url": "https://mostyngriffith.com",
    "email": "mostyn.griffith@gmail.com",
    "linkedin": "https://www.linkedin.com/in/mostyn-griffith/",
    "role": "Staff Product Designer at Login.gov",
    "resume": "assets/mostyn-griffith-resume.pdf",
    "description": "Mostyn Griffith is a product designer making government services more intuitive. "
                   "Staff Product Designer at Login.gov, previously Head of Design at Flare and a designer on IBM Watson.",
    "logo_dark": "CDN/697270276104299a0af9a0ee_pot-black.svg",
    "logo_light": "CDN/68db058c349e84e696157ef4_pot-white.png",
    "og_image": "CDN/68dc3f61e93b92e3999704df_login-5.svg",
    "favicon": "CDN/68dd4dfc403359dde68c60f0_favicon_large.png",
    "touch_icon": "CDN/68dd4dff74e14221cbde3d34_pot_nice.png",
}

# Homepage "About" and experience. Edit freely.
ABOUT = [
    "My work is rooted in the belief that government and civic services should be held to the same standard "
    "as the best consumer products. Access to benefits, healthcare, and public infrastructure shouldn't depend "
    "on someone's patience for a broken interface.",
    "I'm a Staff Product Designer at Login.gov, the federal government's single sign-on service used by over "
    "150 million Americans to access benefits and services. Before moving into civic tech, I was the founding "
    "designer at Flare, taking the product from 0 to 1 and scaling it to 500K+ monthly users across 500+ colleges, "
    "and a Product Designer on IBM Watson Assistant, where I owned the overhaul of the chatbot-building experience "
    "for non-technical users. I also worked with HUSH Studios on experiential design for clients including Uber.",
    "I hold a BFA in Graphic Design with Honors from the Rhode Island School of Design, and I'm based in Brooklyn, NY.",
]
# (organization, role, years)
EXPERIENCE = [
    ("Login.gov", "Staff Product Designer", "2021–Present"),
    ("Flare", "Head of Design / Founding Designer", "2017–2024"),
    ("Native Design", "Senior UX Designer", "2021"),
    ("IBM Watson", "AI Product Designer", "2019–2021"),
    ("HUSH Studios", "Experience Designer", "2018–2021"),
]
EDUCATION = [
    ("Rhode Island School of Design", "BFA Graphic Design with Honors", "2014–2018"),
    ("Brown University", "Coursework in programming and web apps", "2017–2018"),
]
# Big numbers on the homepage. (value, label, case-study slug)
HIGHLIGHTS = [
    ("150M+", "people can use Login.gov to reach government services", "login-help-center"),
    ("55% → 83%", "support calls resolved without an agent", "login-help-center"),
    ("3.6% → 34.5%", "new users protected by 2+ sign-in methods", "login-gov-authentication"),
    ("20K → 150K", "Flare daily active users", "flare"),
]


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)


def local_name(filename):
    name = urllib.parse.unquote(filename)
    return re.sub(r"[^A-Za-z0-9._-]+", "-", name)


def asset(ref, root, video=False):
    """Resolve CDN/<file> (or a bare video filename) to a local or remote URL."""
    if ref.startswith("CDN/"):
        ref = ref[4:]
    elif ref.startswith("http"):
        return ref
    local = ASSETS / local_name(ref)
    if local.exists():
        return f"{root}assets/{local_name(ref)}"
    return (CDN_VIDEO_BASE if video else CDN_BASE) + ref


def inline(text):
    t = esc(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[(.+?)\]\((https?://[^)\s]+|mailto:[^)\s]+)\)",
               r'<a href="\2" rel="noopener">\1</a>', t)
    return t


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")[:60]


def read_page(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta, body = {}, raw
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    meta["tags"] = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
    meta["featured"] = meta.get("featured", "false").lower() == "true"
    meta["order"] = int(meta.get("order", 99))
    meta["stats"] = [
        [p.strip() for p in s.split("|", 1)]
        for s in meta.get("stats", "").split(";;") if "|" in s
    ]
    if "link" in meta:
        url, _, label = meta["link"].partition("|")
        meta["link"] = (url.strip(), label.strip() or url.strip())
    meta["body"] = body
    return meta


# ---------------------------------------------------------------- body renderer
def render_body(body, root):
    lines = body.strip("\n").splitlines()
    out, toc = [], []
    i = 0

    def heading_id(text):
        base = slugify(text) or "section"
        hid, n = base, 2
        while any(t["id"] == hid for t in toc):
            hid, n = f"{base}-{n}", n + 1
        return hid

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1:
                hid = heading_id(text)
                toc.append({"id": hid, "text": text, "part": True})
                out.append(f'<div class="part" id="{hid}"><span class="part__rule"></span>'
                           f'<h2 class="part__title">{inline(text)}</h2></div>')
            elif level == 2:
                hid = heading_id(text)
                toc.append({"id": hid, "text": text, "part": False})
                out.append(f'<h2 id="{hid}">{inline(text)}</h2>')
            elif level == 3:
                cls = ' class="hmw"' if text.lower().startswith("how might we") else ""
                out.append(f"<h3{cls}>{inline(text)}</h3>")
            else:
                out.append(f"<h4>{inline(text)}</h4>")
            i += 1
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:].strip())}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        if line.startswith(">"):
            quote, cite = [], None
            while i < len(lines) and lines[i].startswith(">"):
                t = lines[i][1:].strip()
                if t.startswith("—") or t.startswith("- "):
                    cite = t.lstrip("—- ").strip()
                elif t:
                    quote.append(t)
                i += 1
            c = f"<cite>{inline(cite)}</cite>" if cite else ""
            out.append(f'<blockquote><p>{inline(" ".join(quote))}</p>{c}</blockquote>')
            continue

        if line.startswith("!["):
            figs = []
            while i < len(lines) and lines[i].startswith("!["):
                mm = re.match(r'^!\[(.*?)\]\((\S+?)(?:\s+"(.*)")?\)\s*$', lines[i].strip())
                if mm:
                    alt, src, cap = mm.groups()
                    figs.append((alt, src, cap))
                i += 1
            cls = "media" if len(figs) == 1 else ("media media--grid" if len(figs) % 2 == 0 else "media media--stack")
            inner = []
            for alt, src, cap in figs:
                capt = f"<figcaption>{inline(cap)}</figcaption>" if cap else ""
                inner.append(
                    f'<figure><img src="{asset(src, root)}" alt="{esc(alt)}" loading="lazy" decoding="async">{capt}</figure>')
            out.append(f'<div class="{cls}">{"".join(inner)}</div>')
            continue

        if line.startswith("@video"):
            vids = []
            while i < len(lines) and lines[i].startswith("@video"):
                parts = lines[i].split()
                vids.append((parts[1], parts[2] if len(parts) > 2 else None))
                i += 1
            inner = []
            for src, poster in vids:
                p = f' poster="{asset(poster, root, video=True)}"' if poster else ""
                inner.append(
                    f'<figure class="video"><video autoplay muted loop playsinline preload="metadata"{p}>'
                    f'<source src="{asset(src, root, video=True)}" type="video/mp4"></video>'
                    f'<button class="video__toggle" type="button" aria-label="Pause video">'
                    f'<span aria-hidden="true"></span></button></figure>')
            out.append(f'<div class="media{" media--stack" if len(vids) > 1 else ""}">{"".join(inner)}</div>')
            continue

        if line.startswith("@embed"):
            kind, _, vid = line.split(None, 1)[1].partition(":")
            if kind == "vimeo":
                src = f"https://player.vimeo.com/video/{vid}?dnt=1"
            else:
                src = f"https://www.youtube-nocookie.com/embed/{vid}"
            out.append(f'<div class="media"><div class="embed"><iframe src="{src}" title="Video" loading="lazy" '
                       f'allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div></div>')
            i += 1
            continue

        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,4}\s|- |>|!\[|@)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")

    return "\n".join(out), toc


# ---------------------------------------------------------------- layout
def head(title, description, root, image, path):
    url = SITE["url"] + "/" + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(image)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(image)}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f6f4ef" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121316" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{asset(SITE['favicon'], root)}" type="image/png">
<link rel="apple-touch-icon" href="{asset(SITE['touch_icon'], root)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}static/style.css">
</head>
"""


def header(root, current=""):
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="{root}index.html" aria-label="Mostyn Griffith, home">
      <picture>
        <source srcset="{asset(SITE['logo_light'], root)}" media="(prefers-color-scheme: dark)">
        <img src="{asset(SITE['logo_dark'], root)}" alt="" width="28" height="28">
      </picture>
      <span>Mostyn Griffith</span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="{root}index.html#work"{' aria-current="page"' if current == 'work' else ''}>Work</a>
      <a href="{root}index.html#about">About</a>
      <a href="{root}{SITE['resume']}">Resume</a>
      <a href="{SITE['linkedin']}" rel="noopener">LinkedIn</a>
      <a class="nav__cta" href="mailto:{SITE['email']}">Get in touch</a>
    </nav>
  </div>
</header>
"""


def footer(root):
    return f"""<footer class="site-footer" id="contact">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h2 class="site-footer__title">Have a role or a hard problem in mind?<br><em>Let's talk.</em></h2>
    <div class="site-footer__actions">
      <a class="btn btn--light" href="mailto:{SITE['email']}">{SITE['email']}</a>
      <a class="btn btn--ghost" href="{root}{SITE['resume']}">Resume ↗</a>
      <a class="btn btn--ghost" href="{SITE['linkedin']}" rel="noopener">LinkedIn ↗</a>
    </div>
    <div class="site-footer__meta">
      <span>© <span data-year>2026</span> Mostyn Griffith</span>
      <span>Brooklyn, NY</span>
    </div>
  </div>
</footer>
<script src="{root}static/site.js" defer></script>
</body>
</html>
"""


def tags_html(tags):
    return "".join(f'<li>{esc(t)}</li>' for t in tags)


def work_card(p, root, index, large):
    href = f"{root}work/{p['slug']}/index.html"
    img = asset(p["card"], root)
    title = esc(p.get("short") or p["title"])
    if large:
        return f"""<article class="case">
  <a class="case__media" href="{href}" tabindex="-1" aria-hidden="true">
    <img src="{img}" alt="" loading="{'eager' if index == 1 else 'lazy'}" decoding="async">
  </a>
  <div class="case__body">
    <p class="case__index">{index:02d}{(' · ' + esc(p['years'])) if p.get('years') else ''}</p>
    <ul class="tags">{tags_html(p['tags'])}</ul>
    <h3 class="case__title"><a href="{href}">{title}</a></h3>
    <p class="case__summary">{esc(p['summary'])}</p>
    <p class="case__teaser"><span>Outcome</span>{esc(p.get('teaser', ''))}</p>
    <a class="link-arrow" href="{href}" aria-hidden="true" tabindex="-1">Read case study</a>
  </div>
</article>"""
    return f"""<article class="tile">
  <a href="{href}">
    <div class="tile__media"><img src="{img}" alt="" loading="lazy" decoding="async"></div>
    <ul class="tags">{tags_html(p['tags'])}</ul>
    <h3 class="tile__title">{title}{(' <span class="tile__year">' + esc(p['years']) + '</span>') if p.get('years') else ''}</h3>
    <p class="tile__teaser">{esc(p.get('teaser', ''))}</p>
  </a>
</article>"""


def build_index(pages):
    root = ""
    featured = [p for p in pages if p["featured"]]
    other = [p for p in pages if not p["featured"]]
    by_slug = {p["slug"]: p for p in pages}
    highlights = "".join(
        f'<li><a href="work/{s}/index.html"><strong>{esc(v)}</strong><span>{esc(l)}</span></a></li>'
        for v, l, s in HIGHLIGHTS if s in by_slug)
    cases = "\n".join(work_card(p, root, n, True) for n, p in enumerate(featured, 1))
    tiles = "\n".join(work_card(p, root, 0, False) for p in other)
    about = "".join(f"<p>{esc(a)}</p>" for a in ABOUT)
    def exp_rows(rows):
        return "".join(f'<li><span><strong>{esc(o)}</strong><em>{esc(r)}</em></span><span>{esc(y)}</span></li>'
                       for o, r, y in rows)
    exp = exp_rows(EXPERIENCE)
    edu = exp_rows(EDUCATION)

    page = head("Mostyn Griffith, Product Designer", SITE["description"], root,
                asset(SITE["og_image"], SITE["url"] + "/"), "")
    page += "<body>\n" + header(root)
    page += f"""<main id="main">
  <section class="hero wrap">
    <p class="eyebrow"><span class="dot" aria-hidden="true"></span>{esc(SITE['role'])}</p>
    <h1 class="hero__title">Making government services <em>a little more intuitive</em> for the people who depend on them.</h1>
    <div class="hero__foot">
      <p class="hero__lede">I'm Mostyn, a product designer working across content, interaction and research. At Login.gov I help over 150 million people sign in to the benefits and services they rely on.</p>
      <div class="hero__actions">
        <a class="btn" href="#work">See the work</a>
        <a class="btn btn--ghost" href="mailto:{SITE['email']}">Get in touch</a>
      </div>
    </div>
  </section>

  <section class="highlights wrap" aria-label="Selected impact">
    <ul>{highlights}</ul>
  </section>

  <section class="work wrap" id="work" aria-labelledby="work-title">
    <div class="section-head">
      <p class="eyebrow">Selected work</p>
      <h2 id="work-title" class="section-title">Product case studies</h2>
    </div>
    {cases}
  </section>

  <section class="more wrap" aria-labelledby="more-title">
    <div class="section-head">
      <p class="eyebrow">Also</p>
      <h2 id="more-title" class="section-title">Civic, spatial &amp; brand</h2>
    </div>
    <div class="tiles">
      {tiles}
    </div>
  </section>

  <section class="about wrap" id="about" aria-labelledby="about-title">
    <div class="section-head">
      <p class="eyebrow">About</p>
      <h2 id="about-title" class="section-title">Designing for the moment someone gets stuck.</h2>
    </div>
    <div class="about__grid">
      <div class="about__text">{about}</div>
      <div class="about__side">
        <h3 class="about__label">Experience</h3>
        <ul class="exp">{exp}</ul>
        <h3 class="about__label">Education</h3>
        <ul class="exp">{edu}</ul>
        <h3 class="about__label">Elsewhere</h3>
        <ul class="exp exp--links">
          <li><a href="{SITE['resume']}">Resume (PDF) ↗</a></li>
          <li><a href="{SITE['linkedin']}" rel="noopener">LinkedIn ↗</a></li>
          <li><a href="https://ubiproject.org" rel="noopener">UBIProject.org ↗</a></li>
          <li><a href="mailto:{SITE['email']}">Email ↗</a></li>
        </ul>
      </div>
    </div>
  </section>
</main>
"""
    page += footer(root)
    (ROOT / "index.html").write_text(page, encoding="utf-8")


def build_case(p, nxt):
    root = "../../"
    body, toc = render_body(p["body"], root)
    title = p["title"]
    stats = ""
    if p["stats"]:
        stats = '<ul class="stats">' + "".join(
            f"<li><strong>{esc(v)}</strong><span>{esc(l)}</span></li>" for v, l in p["stats"]) + "</ul>"
    link = ""
    if p.get("link"):
        link = f'<a class="btn btn--ghost" href="{esc(p["link"][0])}" rel="noopener">{esc(p["link"][1])} ↗</a>'
    toc_html = "".join(
        f'<li class="{"toc__part" if t["part"] else ""}"><a href="#{t["id"]}">{inline(t["text"])}</a></li>'
        for t in toc)
    page = head(f"{p.get('short') or title}, Mostyn Griffith", p["summary"], root,
                asset(p["hero"], SITE["url"] + "/"), f"work/{p['slug']}/")
    page += '<body class="is-case">\n' + header(root, "work")
    page += f"""<main id="main">
  <article>
    <header class="case-hero wrap">
      <a class="back" href="{root}index.html#work">← All work</a>
      <ul class="tags">{tags_html(p['tags'])}</ul>
      <h1 class="case-hero__title">{inline(title)}</h1>
      <p class="case-hero__summary">{esc(p['summary'])}</p>
      <dl class="meta">
        <div><dt>My role</dt><dd>{esc(p.get('role', ''))}</dd></div>
        <div><dt>Team</dt><dd>{esc(p.get('team', ''))}</dd></div>
        {('<div><dt>Timeline</dt><dd>' + esc(p['years']) + '</dd></div>') if p.get('years') else ''}
      </dl>
      {stats}
      {link}
    </header>
    <figure class="case-cover wrap"><img src="{asset(p['hero'], root)}" alt="" decoding="async"></figure>
    <div class="case-layout wrap">
      <aside class="toc" aria-label="On this page">
        <p class="toc__label">On this page</p>
        <ol>{toc_html}</ol>
      </aside>
      <div class="prose">
{body}
      </div>
    </div>
  </article>
  <nav class="next wrap" aria-label="Next case study">
    <a href="{root}work/{nxt['slug']}/index.html">
      <span class="eyebrow">Next case study</span>
      <span class="next__title">{esc(nxt.get('short') or nxt['title'])} →</span>
    </a>
  </nav>
</main>
"""
    page += footer(root)
    out = ROOT / "work" / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


def build_404():
    root = "/"
    page = head("Page not found, Mostyn Griffith", SITE["description"], root,
                asset(SITE["og_image"], SITE["url"] + "/"), "404.html")
    page += "<body>\n" + header(root)
    page += """<main id="main" class="wrap notfound">
  <p class="eyebrow">404</p>
  <h1 class="hero__title">This page couldn't be found.</h1>
  <p><a class="btn" href="/">Back to the homepage</a></p>
</main>
"""
    page += footer(root)
    (ROOT / "404.html").write_text(page, encoding="utf-8")


def main():
    pages = sorted((read_page(f) for f in CONTENT.glob("*.md")), key=lambda p: p["order"])
    build_index(pages)
    for n, p in enumerate(pages):
        build_case(p, pages[(n + 1) % len(pages)])
    build_404()
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(pages)} case studies + index.html + 404.html")


if __name__ == "__main__":
    main()
