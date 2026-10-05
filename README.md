# mostyngriffith.com

Portfolio site, rebuilt as a plain static site for GitHub Pages (no Webflow needed).

## How it's organized

- `content/*.md`: one file per case study. Edit text here.
- `build.py`: turns the content into HTML. The homepage intro, About text, experience list and headline numbers live at the top of this file.
- `static/`: stylesheet, script and favicon.
- `assets/`: images and videos (filled by the fetch script, see below).
- `index.html`, `work/*/index.html`, `404.html`: generated pages. Don't edit them by hand; re-run the build.

URLs match the old Webflow site (`/work/login-help-center`, etc.), so existing links keep working.

## One-time setup: download your images and videos

Right now the images still load from Webflow's CDN. To make the site fully independent of Webflow, run this once in Terminal from this folder:

```
python3 scripts/fetch_assets.py
python3 build.py
```

The first command downloads every image and video into `assets/`. The second rebuilds the pages so they point to those local copies.

## Editing

1. Change a file in `content/` (or the settings at the top of `build.py`).
2. Run `python3 build.py`.
3. Preview locally: `python3 -m http.server 8000`, then open http://localhost:8000.

### Content format

```
## Section heading        (appears in the "On this page" sidebar)
# Part heading            (large divider for multi-part case studies)
### / #### Sub-headings   (a "### How might we..." heading gets a highlighted style)
- List item
> Quote text
> — Name, Title
![Alt text](CDN/filename.png "Optional caption")
@video filename.mp4 poster.jpg
@embed vimeo:123456  or  @embed youtube:VIDEOID
**bold**, *italic*, [link](https://example.com)
```

Images on consecutive lines are grouped side by side.

## Publishing on GitHub Pages

1. Create a new repository on GitHub (for example `portfolio`, or `<your-username>.github.io`).
2. From this folder:
   ```
   git init
   git add .
   git commit -m "Portfolio site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo>.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `(root)`**.

### Custom domain (mostyngriffith.com)

1. In **Settings → Pages → Custom domain**, enter `mostyngriffith.com` and save (this adds a `CNAME` file to the repo).
2. At your domain registrar / Cloudflare DNS, remove the old Webflow records and add:
   - Four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - A `CNAME` record for `www` pointing to `<your-username>.github.io`
   - If using Cloudflare, set these records to **DNS only** (grey cloud) until GitHub has issued the HTTPS certificate.
3. Once the certificate is ready, tick **Enforce HTTPS**.
4. Cancel the Webflow site plan only after the new site is live on your domain, and after running the asset download above.
