"""Parses an OpenCollection workspace directory tree into the model in model.py."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

from occdocs.model import Collection, Environment, Folder, GrpcRequest, HttpRequest, Workspace

_SKIP_NAMES = {"opencollection.yml", "folder.yml", ".gitignore", ".DS_Store"}
_KNOWN_REQUEST_TYPES = {"http", "grpc"}


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def parse_workspace(workspace_yml: Path) -> Workspace:
    data = _load_yaml(workspace_yml)
    root = workspace_yml.parent
    info = data.get("info", {})

    collections = []
    for ref in data.get("collections") or []:
        collection_dir = root / ref["path"]
        if not collection_dir.is_dir():
            print(
                f"warning: {workspace_yml}: collection '{ref.get('name')}' points at "
                f"missing path '{ref['path']}', skipping",
                file=sys.stderr,
            )
            continue
        collections.append(parse_collection(collection_dir))

    environments = []
    env_dir = root / "environments"
    if env_dir.is_dir():
        for env_file in sorted(env_dir.glob("*.yml")):
            env_data = _load_yaml(env_file)
            environments.append(
                Environment(
                    name=env_data.get("name", env_file.stem),
                    variables=env_data.get("variables") or [],
                )
            )

    return Workspace(
        name=info.get("name", root.name),
        root=root,
        collections=collections,
        environments=environments,
        docs=data.get("docs") or None,
    )


def parse_collection(collection_dir: Path) -> Collection:
    opencollection_yml = collection_dir / "opencollection.yml"
    data = _load_yaml(opencollection_yml) if opencollection_yml.exists() else {}
    info = data.get("info", {})
    return Collection(
        name=info.get("name", collection_dir.name),
        path=collection_dir,
        children=_parse_children(collection_dir),
    )


def _parse_children(directory: Path) -> list["Folder | HttpRequest | GrpcRequest"]:
    nodes: list[tuple[int, "Folder | HttpRequest | GrpcRequest"]] = []

    for item in sorted(directory.iterdir(), key=lambda p: p.name):
        if item.name in _SKIP_NAMES or item.name.startswith("."):
            continue

        if item.is_dir():
            folder_yml = item / "folder.yml"
            if folder_yml.exists():
                nodes.append(_parse_folder(item, folder_yml))
            continue

        if item.suffix in (".yml", ".yaml"):
            data = _load_yaml(item)
            req_type = (data.get("info") or {}).get("type")
            if req_type == "http":
                nodes.append(_parse_request(item, data))
            elif req_type == "grpc":
                nodes.append(_parse_grpc_request(item, data))
            elif req_type is not None:
                print(f"warning: {item}: unrecognized info.type '{req_type}', skipping", file=sys.stderr)

    nodes.sort(key=lambda pair: pair[0])
    return [node for _, node in nodes]


def _parse_folder(directory: Path, folder_yml: Path) -> tuple[int, Folder]:
    data = _load_yaml(folder_yml)
    info = data.get("info", {})
    docs = (data.get("docs") or {}).get("content")
    folder = Folder(
        name=info.get("name", directory.name),
        seq=info.get("seq", 0),
        docs=docs,
        children=_parse_children(directory),
    )
    return info.get("seq", 0), folder


def _parse_request(path: Path, data: dict) -> tuple[int, HttpRequest]:
    info = data.get("info", {})
    http = data.get("http", {})
    docs = data.get("docs")
    if isinstance(docs, dict):
        docs = docs.get("content")
    request = HttpRequest(
        name=info.get("name", path.stem),
        seq=info.get("seq", 0),
        method=http.get("method", "GET"),
        url=http.get("url", ""),
        params=http.get("params") or [],
        headers=http.get("headers") or [],
        auth=http.get("auth"),
        body=http.get("body"),
        examples=data.get("examples") or [],
        docs=docs,
    )
    return info.get("seq", 0), request


def _parse_grpc_request(path: Path, data: dict) -> tuple[int, GrpcRequest]:
    info = data.get("info", {})
    grpc = data.get("grpc", {})
    docs = data.get("docs")
    if isinstance(docs, dict):
        docs = docs.get("content")
    request = GrpcRequest(
        name=info.get("name", path.stem),
        seq=info.get("seq", 0),
        method=grpc.get("method", ""),
        url=grpc.get("url", ""),
        method_type=grpc.get("methodType", ""),
        proto_file_path=grpc.get("protoFilePath", ""),
        metadata=grpc.get("metadata") or [],
        message=grpc.get("message"),
        auth=grpc.get("auth"),
        docs=docs,
    )
    return info.get("seq", 0), request
