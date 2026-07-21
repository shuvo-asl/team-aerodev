from pathlib import Path

from occdocs import generators  # noqa: F401
from occdocs.discovery import discover_workspace_files
from occdocs.generators.registry import get_generator
from occdocs.mkdocs_writer import build_nav
from occdocs.model import GrpcRequest
from occdocs.parser import parse_workspace

COLLECTIONS_ROOT = Path(__file__).parent.parent / "collections"


def test_discovers_all_sample_workspaces():
    found = discover_workspace_files(COLLECTIONS_ROOT)
    names = {p.parent.name for p in found}
    assert names == {"adsb-backend", "bane-aircraft-service", "bane-invoice-backend"}


def test_parses_bane_aircraft_service_tree():
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-aircraft-service" / "workspace.yml")
    assert workspace.name == "bane-aircraft-service"
    assert len(workspace.collections) == 1
    endpoints = workspace.collections[0]
    assert endpoints.name == "Endpoints"
    folder_names = {child.name for child in endpoints.children}
    assert "Auth" in folder_names
    assert "aircrafts" in folder_names


def test_skips_workspace_collection_with_missing_path(capsys):
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-invoice-backend" / "workspace.yml")
    names = {c.name for c in workspace.collections}
    assert "Authentication" not in names
    assert "Endpoints" in names
    assert "missing path" in capsys.readouterr().err


def test_parses_grpc_requests_not_just_http():
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-aircraft-service" / "workspace.yml")
    endpoints = workspace.collections[0]
    grpc_folder = next(c for c in endpoints.children if c.name == "gRPC")
    assert len(grpc_folder.children) == 10
    assert all(isinstance(child, GrpcRequest) for child in grpc_folder.children)


def test_markdown_generator_writes_grpc_pages(tmp_path):
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-aircraft-service" / "workspace.yml")
    generator = get_generator("markdown")
    generator.generate(workspace, tmp_path)

    grpc_dir = tmp_path / "bane-aircraft-service" / "endpoints" / "grpc"
    assert (grpc_dir / "get-or-create-aircraft.md").exists()
    content = (grpc_dir / "get-or-create-aircraft.md").read_text()
    assert "/bas.BAS/GetOrCreateAircraft" in content


def test_markdown_generator_writes_files_and_nav(tmp_path):
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-aircraft-service" / "workspace.yml")
    generator = get_generator("markdown")
    result = generator.generate(workspace, tmp_path)

    assert (tmp_path / "bane-aircraft-service" / "index.md").exists()
    assert (tmp_path / "bane-aircraft-service" / "endpoints" / "auth" / "login.md").exists()

    nav = build_nav(result.pages)
    assert nav[0]["bane-aircraft-service"]  # top-level workspace entry present


def test_unimplemented_generators_raise_clear_error(tmp_path):
    workspace = parse_workspace(COLLECTIONS_ROOT / "bane-aircraft-service" / "workspace.yml")
    for key in ("openapi", "postman", "html", "pdf"):
        generator = get_generator(key)
        try:
            generator.generate(workspace, tmp_path)
            assert False, f"{key} should not be implemented yet"
        except NotImplementedError:
            pass
