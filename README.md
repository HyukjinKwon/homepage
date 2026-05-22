# HyukjinKwon.github.io

Personal site for Hyukjin Kwon. Static HTML generated from Jinja2 templates,
hosted on GitHub Pages at [hyukjinkwon.github.io](https://hyukjinkwon.github.io/).

## Local development

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python build.py                                # writes to dist/
python -m http.server 8000 --directory dist    # http://localhost:8000
```

Requires Python 3.10+.

## Editing content

All site content lives in [`content.py`](content.py): bio, projects, talks,
publications, social links. Edit that file, re-run `python build.py`, refresh
the browser.

To swap the avatar, change `PROFILE.github` in `content.py` (currently pulled
from `https://github.com/<github>.png`). To use a static file instead, drop it
in `static/` and update `templates/index.html`.

## Deploying

Push to `main`. The workflow at
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) installs Python,
runs `build.py`, and publishes `dist/` via `actions/deploy-pages`.

One-time GitHub setup on the repo:

1. Settings -> Pages -> Build and deployment -> Source: `GitHub Actions`
2. Push to `main` to trigger the first deploy.
3. After it succeeds, Settings -> Pages should show the deployed URL.

## Structure

```
HyukjinKwon.github.io/
    build.py                  renders templates into dist/
    content.py                edit content here
    requirements.txt
    templates/
        base.html             layout
        _header.html
        _footer.html
        _project_card.html    Jinja macro
        index.html
        about.html
        projects.html
        talks.html
        writing.html
        contact.html
    static/                   copied verbatim into dist/
        favicon.svg
        css/global.css
        js/theme.js
    .github/workflows/deploy.yml
```
