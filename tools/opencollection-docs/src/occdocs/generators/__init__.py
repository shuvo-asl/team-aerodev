"""Importing this package registers every built-in generator.

Add a new generator by creating generators/<name>.py (see base.py for
the interface) and adding an import line below -- that's the only
wiring required for it to show up in `occ-docs build --generator ...`.
"""
from occdocs.generators import html, markdown, openapi, pdf, postman  # noqa: F401
