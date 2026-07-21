"""Finds OpenCollection workspaces on disk.

Convention: any workspace.yml found under the collections root is a
project to document. Adding a new project is just adding a new folder
with a workspace.yml under `collections/` -- no registration required.
"""
from __future__ import annotations

from pathlib import Path


def discover_workspace_files(collections_root: Path) -> list[Path]:
    return sorted(collections_root.glob("*/workspace.yml"))
