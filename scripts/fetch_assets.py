#!/usr/bin/env python3
"""
Download every image and video the site uses from the Webflow CDN into ./assets/
so the site no longer depends on Webflow. Run once from the repo root:

  python3 scripts/fetch_assets.py && python3 build.py

Safe to re-run: files that already exist are skipped.
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from build import ASSETS, CDN_BASE, CDN_VIDEO_BASE, local_name  # noqa: E402

refs = {}  # filename -> is_video
sources = list((ROOT / "content").glob("*.md")) + [ROOT / "build.py"]
for f in sources:
    text = f.read_text(encoding="utf-8")
    for m in re.finditer(r"CDN/(\S+?\.(?:png|jpe?g|gif|svg|webp|mp4|webm))(?=[\s)\"']|$)", text):
        refs.setdefault(m.group(1), False)
    for m in re.finditer(r"^@video\s+(\S+)(?:\s+(\S+))?", text, re.M):
        for g in m.groups():
            if g:
                refs[g] = True

ASSETS.mkdir(exist_ok=True)
ok = skipped = failed = 0
for name, is_video in sorted(refs.items()):
    dest = ASSETS / local_name(name)
    if dest.exists() and dest.stat().st_size > 0:
        skipped += 1
        continue
    url = (CDN_VIDEO_BASE if is_video else CDN_BASE) + name
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as out:
            out.write(r.read())
        ok += 1
        print("✓", dest.name)
    except Exception as e:  # noqa: BLE001
        failed += 1
        print("✗", name, "-", e)

print(f"\nDownloaded {ok}, already had {skipped}, failed {failed}.")
if failed:
    print("Failed files will keep loading from the Webflow CDN until fixed.")
