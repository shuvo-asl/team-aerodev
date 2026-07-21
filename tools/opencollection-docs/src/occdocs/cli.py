from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from occdocs import generators  # noqa: F401  (registers built-in generators)
from occdocs.discovery import discover_workspace_files
from occdocs.generators.registry import available_generators, get_generator
from occdocs.mkdocs_writer import build_nav, write_mkdocs_yml
from occdocs.parser import parse_workspace

_GENERATED_MARKER = ".occdocs-generated"

_DEFAULT_INDEX = """# API Documentation

Pick a project from the navigation to browse its endpoints.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="occ-docs")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="Discover collections and generate docs + mkdocs.yml")
    build.add_argument("--collections-root", type=Path, default=Path("collections"))
    build.add_argument("--docs-dir", type=Path, default=Path("docs"))
    build.add_argument("--mkdocs-config", type=Path, default=Path("mkdocs.yml"))
    build.add_argument("--generator", default="markdown")
    build.add_argument("--site-name", default="API Documentation")

    sub.add_parser("list-generators", help="List available generators")

    args = parser.parse_args(argv)

    if args.command == "list-generators":
        for name in available_generators():
            print(name)
        return 0

    return _build(args)


def _build(args: argparse.Namespace) -> int:
    collections_root: Path = args.collections_root
    docs_dir: Path = args.docs_dir

    if not collections_root.is_dir():
        print(f"error: collections root not found: {collections_root}", file=sys.stderr)
        return 1

    workspace_files = discover_workspace_files(collections_root)
    if not workspace_files:
        print(f"warning: no workspace.yml found under {collections_root}", file=sys.stderr)

    generator = get_generator(args.generator)

    docs_dir.mkdir(parents=True, exist_ok=True)
    _clean_previous_output(docs_dir)

    index_md = docs_dir / "index.md"
    if not index_md.exists():
        index_md.write_text(_DEFAULT_INDEX, encoding="utf-8")

    all_pages = []
    for workspace_file in workspace_files:
        workspace = parse_workspace(workspace_file)
        result = generator.generate(workspace, docs_dir)
        all_pages.extend(result.pages)
        for page in result.pages:
            (docs_dir / page.output_path.parts[0] / _GENERATED_MARKER).touch()
        print(f"generated: {workspace.name}")

    nav = [{"Home": "index.md"}, *build_nav(all_pages)]
    write_mkdocs_yml(
        output_path=args.mkdocs_config,
        site_name=args.site_name,
        docs_dir=str(docs_dir),
        nav=nav,
    )
    print(f"wrote {args.mkdocs_config}")
    return 0


def _clean_previous_output(docs_dir: Path) -> None:
    for child in docs_dir.iterdir():
        if child.is_dir() and (child / _GENERATED_MARKER).exists():
            shutil.rmtree(child)


if __name__ == "__main__":
    raise SystemExit(main())
