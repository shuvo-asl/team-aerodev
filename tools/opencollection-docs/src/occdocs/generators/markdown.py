"""OpenCollection -> Markdown generator.

Writes one markdown file per request and one index.md per
folder/collection/workspace, mirroring the OpenCollection tree as a
directory tree under the output root.
"""
from __future__ import annotations

from pathlib import Path

from occdocs.generators.base import GeneratedPage, GenerationResult, Generator
from occdocs.generators.registry import register
from occdocs.model import Collection, Folder, GrpcRequest, HttpRequest, Workspace
from occdocs.slugify import slugify


@register
class MarkdownGenerator(Generator):
    key = "markdown"

    def generate(self, workspace: Workspace, output_root: Path) -> GenerationResult:
        self._output_root = output_root
        ws_slug = slugify(workspace.name)
        ws_dir = output_root / ws_slug
        ws_dir.mkdir(parents=True, exist_ok=True)

        collection_pages = []
        for collection in workspace.collections:
            collection_pages.append(self._write_collection(collection, ws_dir))

        _write(
            ws_dir / "index.md",
            _render_index(
                title=workspace.name,
                intro=workspace.docs,
                entries=[(c.name, f"{slugify(c.name)}/index.md") for c in workspace.collections],
                entry_heading="Collections",
            ),
        )

        if workspace.environments:
            env_lines = [f"# {workspace.name} — Environments", ""]
            for env in workspace.environments:
                env_lines.append(f"## {env.name}")
                env_lines.append("")
                env_lines.append("| Variable | Value |")
                env_lines.append("|---|---|")
                for var in env.variables:
                    env_lines.append(f"| `{var.get('name', '')}` | `{var.get('value', '')}` |")
                env_lines.append("")
            _write(ws_dir / "environments.md", "\n".join(env_lines))

        root_page = GeneratedPage(title=workspace.name, output_path=self._rel(ws_dir / "index.md"))
        root_page.children.extend(collection_pages)
        if workspace.environments:
            root_page.children.append(
                GeneratedPage(title="Environments", output_path=self._rel(ws_dir / "environments.md"))
            )

        return GenerationResult(workspace_name=workspace.name, pages=[root_page])

    def _write_collection(self, collection: Collection, ws_dir: Path) -> GeneratedPage:
        col_slug = slugify(collection.name)
        col_dir = ws_dir / col_slug
        col_dir.mkdir(parents=True, exist_ok=True)

        child_pages = [self._write_node(child, col_dir) for child in collection.children]

        _write(
            col_dir / "index.md",
            _render_index(
                title=collection.name,
                intro=None,
                entries=_entries_for_nav(collection.children),
                entry_heading="Contents",
            ),
        )

        page = GeneratedPage(title=collection.name, output_path=self._rel(col_dir / "index.md"))
        page.children = child_pages
        return page

    def _write_node(self, node, parent_dir: Path) -> GeneratedPage:
        if isinstance(node, Folder):
            return self._write_folder(node, parent_dir)
        if isinstance(node, GrpcRequest):
            return self._write_grpc_request(node, parent_dir)
        return self._write_request(node, parent_dir)

    def _write_folder(self, folder: Folder, parent_dir: Path) -> GeneratedPage:
        slug = slugify(folder.name)
        folder_dir = parent_dir / slug
        folder_dir.mkdir(parents=True, exist_ok=True)

        child_pages = [self._write_node(child, folder_dir) for child in folder.children]

        _write(
            folder_dir / "index.md",
            _render_index(
                title=folder.name,
                intro=folder.docs,
                entries=_entries_for_nav(folder.children),
                entry_heading="Contents",
            ),
        )

        page = GeneratedPage(title=folder.name, output_path=self._rel(folder_dir / "index.md"))
        page.children = child_pages
        return page

    def _write_request(self, request: HttpRequest, parent_dir: Path) -> GeneratedPage:
        slug = slugify(request.name)
        file_path = parent_dir / f"{slug}.md"
        _write(file_path, _render_request(request))
        return GeneratedPage(title=request.name, output_path=self._rel(file_path))

    def _write_grpc_request(self, request: GrpcRequest, parent_dir: Path) -> GeneratedPage:
        slug = slugify(request.name)
        file_path = parent_dir / f"{slug}.md"
        _write(file_path, _render_grpc_request(request))
        return GeneratedPage(title=request.name, output_path=self._rel(file_path))

    def _rel(self, absolute_path: Path) -> Path:
        return absolute_path.relative_to(self._output_root)


def _entries_for_nav(children) -> list[tuple[str, str]]:
    entries = []
    for child in children:
        slug = slugify(child.name)
        if isinstance(child, Folder):
            entries.append((child.name, f"{slug}/index.md"))
        else:
            entries.append((child.name, f"{slug}.md"))
    return entries


def _render_index(title: str, intro: str | None, entries: list[tuple[str, str]], entry_heading: str) -> str:
    lines = [f"# {title}", ""]
    if intro:
        lines.append(intro)
        lines.append("")
    if entries:
        lines.append(f"## {entry_heading}")
        lines.append("")
        for name, link in entries:
            lines.append(f"- [{name}]({link})")
        lines.append("")
    return "\n".join(lines)


def _render_request(request: HttpRequest) -> str:
    lines = [f"# {request.name}", "", f"**{request.method}** `{request.url}`", ""]

    if request.docs:
        lines.append(request.docs)
        lines.append("")

    if request.auth:
        lines.append("## Auth")
        lines.append("")
        lines.append(f"Type: `{request.auth.get('type', 'inherit') if isinstance(request.auth, dict) else request.auth}`")
        lines.append("")

    if request.params:
        lines.append("## Query Params")
        lines.append("")
        lines.append("| Name | Value | Type |")
        lines.append("|---|---|---|")
        for p in request.params:
            lines.append(f"| `{p.get('name', '')}` | `{p.get('value', '')}` | {p.get('type', '')} |")
        lines.append("")

    if request.headers:
        lines.append("## Headers")
        lines.append("")
        lines.append("| Name | Value |")
        lines.append("|---|---|")
        for h in request.headers:
            lines.append(f"| `{h.get('name', '')}` | `{h.get('value', '')}` |")
        lines.append("")

    if request.body:
        body_type = request.body.get("type", "")
        data = request.body.get("data", "")
        lines.append("## Body")
        lines.append("")
        lines.append(f"Type: `{body_type}`")
        lines.append("")
        if data:
            lang = "json" if body_type == "json" else ""
            lines.append(f"```{lang}")
            lines.append(str(data).rstrip())
            lines.append("```")
            lines.append("")

    if request.examples:
        lines.append("## Examples")
        lines.append("")
        for example in request.examples:
            lines.append(f"### {example.get('name', 'Example')}")
            lines.append("")
            req = example.get("request", {})
            resp = example.get("response", {})
            if req:
                lines.append(f"**Request:** `{req.get('method', request.method)}` `{req.get('url', request.url)}`")
                lines.append("")
                req_body = (req.get("body") or {}).get("data")
                if req_body:
                    lines.append("```json")
                    lines.append(str(req_body).rstrip())
                    lines.append("```")
                    lines.append("")
            if resp:
                status = resp.get("status", "")
                status_text = resp.get("statusText", "")
                lines.append(f"**Response:** `{status} {status_text}`".rstrip())
                lines.append("")
                resp_body = (resp.get("body") or {}).get("data")
                if resp_body:
                    lines.append("```json")
                    lines.append(str(resp_body).rstrip())
                    lines.append("```")
                    lines.append("")

    return "\n".join(lines)


def _render_grpc_request(request: GrpcRequest) -> str:
    lines = [f"# {request.name}", "", f"**gRPC** ({request.method_type}) `{request.method}`", "", f"Endpoint: `{request.url}`", ""]

    if request.docs:
        lines.append(request.docs)
        lines.append("")

    if request.proto_file_path:
        lines.append(f"Proto file: `{request.proto_file_path}`")
        lines.append("")

    if request.auth:
        lines.append("## Auth")
        lines.append("")
        lines.append(f"Type: `{request.auth.get('type', 'inherit') if isinstance(request.auth, dict) else request.auth}`")
        lines.append("")

    if request.metadata:
        lines.append("## Metadata")
        lines.append("")
        lines.append("| Name | Value |")
        lines.append("|---|---|")
        for m in request.metadata:
            lines.append(f"| `{m.get('name', '')}` | `{m.get('value', '')}` |")
        lines.append("")

    if request.message:
        lines.append("## Message")
        lines.append("")
        lines.append("```json")
        lines.append(str(request.message).rstrip())
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
