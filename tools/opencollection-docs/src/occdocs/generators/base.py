"""The plug point new generators implement.

To add a new output format (OpenAPI, Postman, HTML, PDF, ...):
  1. Create generators/<name>.py with a class implementing Generator.
  2. Set `key` to a unique CLI-facing name.
  3. Decorate it with @register.
  4. Import the module from generators/__init__.py so it registers itself.

Nothing else needs to change -- discovery, parsing, and the CLI are
generator-agnostic.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path

from occdocs.model import Workspace


@dataclass
class GeneratedPage:
    """One node in the output nav tree.

    `output_path` is relative to the docs root and is None for pages
    that exist purely to group children in the nav (no content of
    their own).
    """

    title: str
    output_path: Path | None = None
    children: list["GeneratedPage"] = field(default_factory=list)


@dataclass
class GenerationResult:
    workspace_name: str
    pages: list[GeneratedPage] = field(default_factory=list)


class Generator(ABC):
    """Base class for all OpenCollection -> <format> generators."""

    key: str

    @abstractmethod
    def generate(self, workspace: Workspace, output_root: Path) -> GenerationResult:
        """Render `workspace` into files under `output_root`.

        Must return the nav structure for the pages it wrote so the
        mkdocs.yml writer can build navigation without knowing
        anything about the generator's internals.
        """
        raise NotImplementedError
