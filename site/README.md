# NetLab Static Site

Browser-facing showcase for the repository.

## What It Contains

- `index.html`: product-style landing page with project overview and interactive demos.
- `projects/*.html`: browser-ready documentation pages for each experiment.
- `scripts.js`: checksum and parity demo logic.
- `styles.css`: shared visual system for the landing page and project pages.

## Why The Project Pages Exist

Static sites should route users to HTML documents, not raw Markdown files from the source tree.
The project cards therefore link to pages under `site/projects/` instead of `projects/*/README.md`.

## Local Preview

```bash
python -m http.server 8080 --directory site
```
