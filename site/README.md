# GitHub Pages Site

Static showcase entrypoint for this repository.

## Local Preview

Open `site/index.html` directly in a browser, or serve with a static server:

```bash
python -m http.server 8080 --directory site
```

## Deploy

- Ensure default branch is `main`.
- Enable GitHub Pages source as **GitHub Actions**.
- The workflow `.github/workflows/pages.yml` deploys the `site/` folder.
