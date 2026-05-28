# Mostyn Griffith — Portfolio (GitHub Pages)

Static portfolio site for [mostyngriffith.com](https://www.mostyngriffith.com/), rebuilt from the Webflow site as plain HTML and CSS.

## Structure

- `index.html` — Homepage (intro, project grid, contact)
- `css/site.css` — Homepage styles
- `images/` — Logo, favicon, and project thumbnails
- `work/<slug>/` — Case study URLs (match Webflow paths; redirect to `content/` pages for now)
- `content/` — Full case study pages and assets (legacy layout)

## Local preview

```bash
cd mostyng.github.io
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Deploy to GitHub Pages

1. Push this repo to `github.com/mostyng/mostyng.github.io` on the `master` branch.
2. In the repo on GitHub: **Settings → Pages**
   - **Source:** Deploy from branch
   - **Branch:** `master` / `/ (root)`
3. Confirm `CNAME` contains `www.mostyngriffith.com`.
4. In your DNS provider, point `www` (and optionally apex) to GitHub Pages ([docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)).

After DNS propagates, the custom domain serves this site instead of Webflow.

## Migrating off Webflow

1. Deploy and verify the GitHub Pages site on the custom domain.
2. When satisfied, cancel or unpublish the Webflow project.
3. Optional next steps:
   - Move case studies from `content/` into `work/<slug>/` with the new `site.css` layout
   - Export remaining Webflow case study copy and media into `content/` or `work/`

## Custom domain

`CNAME` is set to `www.mostyngriffith.com`. Do not remove it unless you change domains.
