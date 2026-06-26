# -*- coding: utf-8 -*-
"""
Rewrite relative image paths in article/page content to {static}/... paths.

When ARTICLE_SAVE_AS uses flat {slug}.html URLs, Markdown preview resolves
images relative to the source file, but the generated HTML resolves them
relative to the output root. This plugin bridges that gap at build time.
"""

import logging
import os

from bs4 import BeautifulSoup
from pelican import contents, signals

logger = logging.getLogger(__name__)

_SKIP_PREFIXES = (
    "http://",
    "https://",
    "//",
    "data:",
    "/",
    "#",
    "{",
    "mailto:",
)


def _should_skip(src):
    if not src or not src.strip():
        return True
    return src.startswith(_SKIP_PREFIXES)


def _resolve_static_url(content, src):
    article_dir = content.relative_dir
    if not article_dir:
        return None

    content_root = os.path.abspath(content.settings["PATH"])
    candidate = os.path.normpath(
        os.path.join(content_root, article_dir, src.replace("/", os.sep))
    )
    if not candidate.startswith(content_root) or not os.path.isfile(candidate):
        return None

    rel_path = os.path.relpath(candidate, content_root).replace(os.sep, "/")
    return "{static}/" + rel_path


def fix_relative_images(content):
    if isinstance(content, contents.Static):
        return
    if not content._content or not content.source_path:
        return

    soup = BeautifulSoup(content._content, "html.parser")
    changed = False

    for img in soup.find_all("img"):
        src = img.get("src")
        if _should_skip(src):
            continue

        new_src = _resolve_static_url(content, src)
        if new_src:
            img["src"] = new_src
            changed = True
        else:
            logger.warning(
                "relative_images: image not found for %s: %s",
                content.get_relative_source_path(),
                src,
            )

    if changed:
        content._content = str(soup)


def register():
    signals.content_object_init.connect(fix_relative_images)
