"""In-memory representation of a parsed OpenCollection tree.

An OpenCollection workspace (workspace.yml) references one or more
collections (opencollection.yml). Each collection is a tree of folders
(folder.yml) and http requests (any other *.yml with info.type: http).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class HttpRequest:
    name: str
    seq: int
    method: str
    url: str
    params: list[dict] = field(default_factory=list)
    headers: list[dict] = field(default_factory=list)
    auth: dict | None = None
    body: dict | None = None
    examples: list[dict] = field(default_factory=list)
    docs: str | None = None


@dataclass
class GrpcRequest:
    name: str
    seq: int
    method: str
    url: str
    method_type: str = ""
    proto_file_path: str = ""
    metadata: list[dict] = field(default_factory=list)
    message: str | None = None
    auth: dict | None = None
    docs: str | None = None


@dataclass
class Folder:
    name: str
    seq: int
    docs: str | None = None
    children: list["Node"] = field(default_factory=list)


Node = Folder | HttpRequest | GrpcRequest


@dataclass
class Collection:
    """A collection root (opencollection.yml) and its child tree."""

    name: str
    path: Path
    children: list[Node] = field(default_factory=list)


@dataclass
class Environment:
    name: str
    variables: list[dict] = field(default_factory=list)


@dataclass
class Workspace:
    """A workspace.yml — one documentation "project" (e.g. bane-invoice-backend)."""

    name: str
    root: Path
    collections: list[Collection] = field(default_factory=list)
    environments: list[Environment] = field(default_factory=list)
    docs: str | None = None
