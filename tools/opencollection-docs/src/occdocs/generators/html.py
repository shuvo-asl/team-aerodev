from __future__ import annotations

from pathlib import Path

from occdocs.generators.base import GenerationResult, Generator
from occdocs.generators.registry import register
from occdocs.model import Workspace


@register
class HtmlGenerator(Generator):
    key = "html"

    def generate(self, workspace: Workspace, output_root: Path) -> GenerationResult:
        raise NotImplementedError(
            "The 'html' generator is registered but not implemented yet. "
            "Implement HtmlGenerator.generate() in generators/html.py."
        )
