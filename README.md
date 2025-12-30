# Annolid Website + Jupyter Book (Publishing Guide)

This folder (`book/healthonrails.github.io/`) is a separate git repository that deploys the Annolid website and Jupyter Book to GitHub Pages (custom domain: `annolid.com`).

The repo uses two branches:

- `main`: Jupyter Book *sources* + a built copy of the book under `html/` (useful for review / diffing).
- `gh-pages`: the *published* site root (what GitHub Pages serves). This contains the website landing page (`index.html` + `assets/`) and the Jupyter Book output folders (`content/`, `tutorials/`, `_static/`, `_sources/`, etc.).

## Prerequisites

- Python 3.9+ (3.10+ recommended)
- Git

From the Annolid repo root, you can run all commands with `git -C book/healthonrails.github.io …`.

## Update Jupyter Book content (sources)

Edit/add pages here:

- `content/*.md`
- `tutorials/*.md` (or notebooks if you enable execution)
- `_toc.yml` (navigation)
- `_config.yml` (book config)
- `images/` (book images)

Tip: keep filenames stable whenever possible because GitHub Pages URLs are filename-based (e.g. `content/how_to_install.html`).

## Build the book locally

Build uses `jupyter-book` and writes output to `_build/html/`.

```bash
cd book/healthonrails.github.io
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

jupyter-book build .
```

Optional: open the local build:

```bash
open _build/html/index.html
```

## Update `main` branch build artifacts (`html/`)

We keep a copy of the generated site under `html/` on `main` for easy review and to make publishing reproducible.

```bash
cd book/healthonrails.github.io
git checkout main

jupyter-book build .
rsync -a --delete _build/html/ html/

git add -A
git commit -m "Update Jupyter Book sources and rebuild"
git push origin main
```

## Publish to GitHub Pages (`gh-pages` branch)

Publishing means copying the built HTML into the `gh-pages` branch root.

Important: the `gh-pages` branch also hosts the website landing page. When syncing book output, do **not** overwrite:

- `index.html` (landing page)
- `assets/` (landing page assets)
- `CNAME` (custom domain)

Recommended workflow:

```bash
cd book/healthonrails.github.io

# Build on main (or rebuild if needed)
git checkout main
jupyter-book build .

# Copy build output aside so it survives the branch switch
tmp_dir="$(mktemp -d)"
rsync -a --delete _build/html/ "${tmp_dir}/"

# Switch to the published branch and sync, preserving the landing page
git checkout gh-pages
rsync -a --delete \
  --exclude 'index.html' \
  --exclude 'assets/' \
  --exclude 'CNAME' \
  "${tmp_dir}/" .

# Critical: ensures GitHub Pages serves `_static/`, `_sources/`, etc.
touch .nojekyll

git add -A
git commit -m "Publish Jupyter Book"
git push origin gh-pages

# Return to main for normal work
git checkout main
```

## Verify the deployment

After GitHub Pages finishes rebuilding (can take ~1–2 minutes), verify that the book CSS loads:

```bash
curl -I https://annolid.com/_static/styles/theme.css
```

If this returns `404`, the most common issue is missing `.nojekyll` on the published root (`gh-pages`).

## Troubleshooting

- **Book pages are unstyled / CSS missing**
  - Ensure `gh-pages` contains `.nojekyll` at the repo root.
  - Confirm `_static/` exists in the `gh-pages` branch root.
- **Accidentally overwrote the landing page**
  - Restore `index.html` and `assets/` on `gh-pages` from git history, then re-run the publish step with the excludes.
- **Broken links after renaming files**
  - Prefer leaving old pages in place or adding a small “moved” page to preserve existing URLs.

