#!/usr/bin/env python3
"""Build the personal homepage as static HTML in dist/.

Usage:
    python build.py

Preview locally:
    python -m http.server 8000 --directory dist
"""
from __future__ import annotations

import json
import os
import shutil
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
OUT_DIR = ROOT / "dist"

# (template name, output path relative to dist/, current-nav marker)
PAGES: list[tuple[str, str, str]] = [
    ("index.html", "index.html", "/"),
    ("about.html", "about/index.html", "/about/"),
    ("projects.html", "projects/index.html", "/projects/"),
    ("talks.html", "talks/index.html", "/talks/"),
    ("writing.html", "writing/index.html", "/writing/"),
    ("diving.html", "diving/index.html", "/diving/"),
    ("contact.html", "contact/index.html", "/contact/"),
]


def site_base_path() -> str:
    """Root path prefix for GitHub Pages project sites, e.g. /homepage."""
    override = os.environ.get("SITE_BASE_PATH")
    if override is not None:
        return override.rstrip("/")

    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not repo:
        return ""

    name = repo.split("/", 1)[-1]
    if name.endswith(".github.io"):
        return ""
    return f"/{name}"


def url_for(path: str, *, base: str | None = None) -> str:
    prefix = site_base_path() if base is None else base.rstrip("/")
    if not path.startswith("/"):
        path = f"/{path}"
    if path == "/":
        return f"{prefix}/" if prefix else "/"
    return f"{prefix}{path}" if prefix else path


def build() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["url_for"] = url_for

    dive_sites_json = json.dumps([asdict(s) for s in content.DIVE_SITES])
    base = site_base_path()

    base_ctx = {
        "profile": content.PROFILE,
        "projects": content.PROJECTS,
        "talks": content.TALKS,
        "blog_posts": content.BLOG_POSTS,
        "about_bio": content.ABOUT_BIO,
        "dive_sites": content.DIVE_SITES,
        "dive_sites_json": dive_sites_json,
        "nav_links": [
            (url_for(href, base=base), label) for href, label in content.NAV_LINKS
        ],
        "now_year": datetime.now().year,
    }

    for template_name, output_path, current in PAGES:
        out = OUT_DIR / output_path
        out.parent.mkdir(parents=True, exist_ok=True)
        rendered = env.get_template(template_name).render(
            **base_ctx, current=url_for(current, base=base)
        )
        out.write_text(rendered, encoding="utf-8")
        print(f"  rendered  {template_name:25s}  ->  dist/{output_path}")

    for item in STATIC_DIR.iterdir():
        dest = OUT_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)
        print(f"  copied    {item.name}")

    print(f"\nBuilt {len(PAGES)} pages to {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
