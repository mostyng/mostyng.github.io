#!/usr/bin/env python3
"""Migrate Webflow case study pages to work/<slug>/index.html with local assets."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO = Path(__file__).resolve().parents[1]
WORK = REPO / "work"
SITE_ID = "68d9d5fedda8c841de1ca7fb"
CDN_PREFIX = f"https://cdn.prod.website-files.com/{SITE_ID}/"
CDN_ENCODED = f"https://cdn.prod.website-files.com/{SITE_ID}%2F"

SLUGS = [
    "login-help-center",
    "login-gov-security-key-improvements",
    "login-gov-authentication",
    "flare",
    "ibm-watson-assistant",
    "atelier-nido",
    "tia-carmen",
    "uber",
]

SKIP_URL_SUBSTRINGS = (
    "6022af993a6b2191db3ed10c",  # generic Webflow video UI icons
    "d3e54v103j8qbb.cloudfront.net",
)


def fetch(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    # curl treats spaces as URL delimiters, so encode them.
    url = url.replace(" ", "%20")
    try:
        subprocess.run(
            ["curl", "-fsSL", url, "-o", str(dest)],
            check=True,
            capture_output=True,
            timeout=120,
        )
        return dest.exists() and dest.stat().st_size > 0
    except subprocess.CalledProcessError:
        print(f"  WARN: failed to download {url}", file=sys.stderr)
        return False


def url_to_filename(url: str) -> str:
    url = unquote(url.split("?")[0])
    path = urlparse(url).path
    name = path.split("/")[-1]
    if not name or "." not in name:
        digest = hashlib.md5(url.encode()).hexdigest()[:10]
        ext = ".mp4" if ".mp4" in url.lower() else ".bin"
        name = f"asset-{digest}{ext}"
    name = re.sub(r"[^\w.\-]", "_", name)
    return name


def should_mirror(url: str) -> bool:
    if any(s in url for s in SKIP_URL_SUBSTRINGS):
        return False
    return SITE_ID in url or f"{SITE_ID}%2F" in url


def extract_main_content(html: str) -> str:
    body_m = re.search(r"<body[^>]*>(.*)</body>", html, re.DOTALL | re.IGNORECASE)
    if not body_m:
        raise ValueError("no body")
    body = body_m.group(1)
    body = re.sub(r"<script[\s\S]*?</script>", "", body, flags=re.IGNORECASE)

    # Content starts at hero section (after nav)
    start_m = re.search(r'<div class="section hero"', body)
    if not start_m:
        start_m = re.search(r'<div class="section[^"]*">\s*<img', body)
    if not start_m:
        raise ValueError("no hero section")
    start = start_m.start()

    # End before footer contact (keep one contact at end via template — strip webflow duplicate)
    end = body.find('<div class="section cc-contact">', start)
    if end == -1:
        end = len(body)
    return body[start:end]


def convert_videos(html: str, assets_dir: Path, url_map: dict[str, str]) -> str:
    """Replace Webflow background video widgets with simple HTML5 video blocks."""

    def repl(match: re.Match) -> str:
        block = match.group(0)
        mp4s = re.findall(
            rf"https://cdn\.prod\.website-files\.com/{SITE_ID}(?:%2F|/)[^\s\"']+\.mp4",
            block,
            flags=re.IGNORECASE,
        )
        if not mp4s:
            return ""
        mp4 = unquote(mp4s[0])
        local = url_map.get(mp4)
        if not local:
            return ""
        poster_m = re.search(r"data-poster-url=\"([^\"]+)\"", block)
        poster_attr = ""
        if poster_m:
            poster_url = unquote(poster_m.group(1))
            poster_local = url_map.get(poster_url)
            if poster_local:
                poster_attr = f' poster="{poster_local}"'
        return (
            f'<div class="media-video-wrap">'
            f'<video class="media-video" autoplay loop muted playsinline{poster_attr}>'
            f'<source src="{local}" type="video/mp4">'
            f"</video></div>"
        )

    # Remove noscript + control buttons inside video blocks by replacing whole widget
    pattern = re.compile(
        r'<div class="div-video[^"]*">.*?class="[^"]*w-background-video[^"]*">.*?</div>\s*</div>',
        re.DOTALL,
    )
    html = pattern.sub(repl, html)
    return html


def clean_html(html: str) -> str:
    html = unescape(html)
    html = re.sub(r"\s+srcset=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+sizes=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+data-w-[a-z-]+=\"[^\"]*\"", "", html, flags=re.IGNORECASE)
    html = re.sub(r"\s+data-wf-[a-z-]+=\"[^\"]*\"", "", html, flags=re.IGNORECASE)
    html = re.sub(r'\s+id="w-node-[^"]*"', "", html)
    html = re.sub(r"\s+data-poster-url=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+data-video-urls=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+data-autoplay=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+data-loop=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+aria-[a-z-]+=\"[^\"]*\"", "", html)
    html = re.sub(r"<noscript>[\s\S]*?</noscript>", "", html, flags=re.IGNORECASE)
    html = re.sub(
        r'<div aria-live="polite">[\s\S]*?</div>\s*</div>\s*</div>',
        "</div></div>",
        html,
        flags=re.IGNORECASE,
    )
    html = re.sub(r"\s+loading=\"[^\"]*\"", "", html)
    html = re.sub(r"\s+width=\"\d+\"", "", html)
    html = re.sub(r'class="[^"]*\bw-background-video[^"]*"', 'class="media-video-legacy"', html)
    html = re.sub(r"\bw-inline-block\b", "", html)
    html = re.sub(r'\s+class="\s*"', "", html)
    html = re.sub(r'class="\s+', 'class="', html)
    html = re.sub(r'\s{2,}', " ", html)
    html = re.sub(r'href="/"', 'href="../../"', html)
    html = re.sub(r"&#x27;", "'", html)
    return html.strip()


def mirror_assets(html: str, assets_dir: Path) -> tuple[str, dict[str, str]]:
    url_map: dict[str, str] = {}
    urls: set[str] = set()

    for m in re.finditer(
        rf"https://cdn\.prod\.website-files\.com/{SITE_ID}(?:%2F|/)[^\s\"')]+",
        html,
        flags=re.IGNORECASE,
    ):
        raw = m.group(0)
        # Webflow stores multiple URLs in a single attribute, comma-separated.
        for part in raw.split(","):
            part = part.strip().strip('"').strip("'").strip()
            if not part:
                continue
            urls.add(unquote(part))

    for url in sorted(urls):
        if not should_mirror(url):
            continue
        fname = url_to_filename(url)
        dest = assets_dir / fname
        if fetch(url, dest):
            rel = f"assets/{fname}"
            url_map[url] = rel

    def sub_url(m: re.Match) -> str:
        raw = m.group(0)
        decoded = unquote(raw)
        for candidate in (raw, decoded):
            if candidate in url_map:
                return url_map[candidate]
        return raw

    html = re.sub(
        rf"https://cdn\.prod\.website-files\.com/{SITE_ID}(?:%2F|/)[^\s\"')]+",
        sub_url,
        html,
        flags=re.IGNORECASE,
    )
    return html, url_map


def build_page(title: str, description: str, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Mostyn Griffith</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="../../css/case-study.css">
  <link rel="icon" type="image/png" href="../../images/favicon.png">
</head>
<body class="case-study">
  <header class="site-nav site-nav--light" role="banner">
    <div class="site-nav__inner">
      <a href="../../" class="logo-link">
        <img src="../../images/pot-black.svg" alt="Mostyn Griffith home" class="logo-image" width="40" height="40">
      </a>
    </div>
  </header>

  <main class="case-study-main">
{content}
  </main>

  <footer class="case-study-footer">
    <div class="contact">
      <h3 class="contact-headline">Interested in collaborating?<br>Schedule a free consultation.</h3>
      <p class="p-contact">Contact <a href="mailto:mostyn.griffith@gmail.com?subject=Portfolio%20inquiry">mostyn.griffith@gmail.com</a></p>
    </div>
  </footer>
  <script src="../../js/nav-collapse.js"></script>
</body>
</html>
"""


def migrate_slug(slug: str) -> None:
    src = Path(f"/tmp/wf-{slug}.html")
    if not src.exists():
        fetch(f"https://www.mostyngriffith.com/work/{slug}", src)

    html = src.read_text(encoding="utf-8", errors="replace")
    title_m = re.search(r"<title>([^<]+)</title>", html)
    title = title_m.group(1).strip() if title_m else slug
    desc_m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', html)
    description = (desc_m.group(1) if desc_m else title).replace('"', "&quot;")

    out_dir = WORK / slug
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    content = extract_main_content(html)
    # Decode entities early so URLs don't contain &quot; etc.
    content = unescape(content)
    content, url_map = mirror_assets(content, assets_dir)
    content = convert_videos(content, assets_dir, url_map)
    content = clean_html(content)

    indented = "\n".join("    " + line for line in content.split("\n"))
    page = build_page(title, description, indented)

    (out_dir / "index.html").write_text(page, encoding="utf-8")
    asset_count = len(list(assets_dir.glob("*")))
    print(f"OK {slug}: {asset_count} assets, {len(page)} bytes html")


def main() -> None:
    for slug in SLUGS:
        migrate_slug(slug)


if __name__ == "__main__":
    main()
