from __future__ import annotations

import re

_NON_SLUG = re.compile(r"[^a-z0-9]+")


def slugify(name: str) -> str:
    slug = _NON_SLUG.sub("-", name.strip().lower()).strip("-")
    return slug or "untitled"
