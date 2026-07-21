# opencollection-docs

Generates a documentation site from [OpenCollection](https://github.com/usebruno/bruno)
API collections (Bruno's `workspace.yml` / `opencollection.yml` /
`folder.yml` / per-request `.yml` format).

Convention over configuration: drop a project's OpenCollection export
under `collections/<project-name>/`, run `occ-docs build`, and it
appears in the docs site automatically. `mkdocs.yml` is a **build
artifact** — it's regenerated and overwritten on every run, so no one
edits it by hand or forgets to wire up a new project's nav.

## Layout

```
collections/<project>/workspace.yml   OpenCollection export, one per project (input, not generated)
docs/                                  generated markdown + docs/index.md (handwritten landing page)
mkdocs.yml                             generated — do not hand-edit, it's overwritten every build
src/occdocs/                           the generator
  model.py                             parsed representation of a workspace/collection/folder/request
  parser.py                            OpenCollection YAML -> model.py
  discovery.py                         finds collections/*/workspace.yml
  generators/                          one module per output format (the extension point)
    base.py                            Generator ABC + GeneratedPage/GenerationResult
    registry.py                        @register decorator, get_generator(), available_generators()
    markdown.py                        implemented: OpenCollection -> Markdown
    openapi.py, postman.py, html.py, pdf.py   registered stubs, NotImplementedError until built
  mkdocs_writer.py                     turns GeneratedPage trees into mkdocs.yml nav
  cli.py                               `occ-docs build` / `occ-docs list-generators`
```

## Usage

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[site,dev]"

occ-docs build --site-name "ASL API Documentation"   # writes docs/ and mkdocs.yml
mkdocs serve                                          # preview at http://127.0.0.1:8000
```

Adding a new project: copy its OpenCollection export into
`collections/<name>/` (must contain `workspace.yml`) and re-run
`occ-docs build`. No other file needs to change.

## Adding a new generator

1. Create `src/occdocs/generators/<name>.py`:

   ```python
   from occdocs.generators.base import Generator, GenerationResult
   from occdocs.generators.registry import register

   @register
   class MyGenerator(Generator):
       key = "myformat"

       def generate(self, workspace, output_root):
           ...  # write files under output_root, return GenerationResult(pages=[...])
   ```

2. Import the module from `src/occdocs/generators/__init__.py`.
3. Run `occ-docs build --generator myformat`.

Generators that produce a single combined file per workspace (OpenAPI,
Postman, PDF) don't need to build a nav tree — return a
`GenerationResult` with one `GeneratedPage` pointing at that file.
Generators that produce a page per request (Markdown, HTML) build the
nested `GeneratedPage` tree the way `markdown.py` does; `mkdocs_writer`
only cares about the tree shape, not which generator produced it.

## Known data quirks

Some existing OpenCollection exports have stale `workspace.yml`
`collections:` entries pointing at paths that no longer exist (leftover
from reorganizing in Bruno). The parser logs a warning and skips them
rather than failing the whole build.
