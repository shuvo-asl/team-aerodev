from __future__ import annotations

from pathlib import Path

from occdocs.generators.base import GenerationResult, Generator
from occdocs.generators.registry import register
from occdocs.model import Workspace


@register
class PdfGenerator(Generator):
    key = "pdf"

    def generate(self, workspace: Workspace, output_root: Path) -> GenerationResult:
        raise NotImplementedError(
            "The 'pdf' generator is registered but not implemented yet. "
            "Implement PdfGenerator.generate() in generators/pdf.py."
        )
