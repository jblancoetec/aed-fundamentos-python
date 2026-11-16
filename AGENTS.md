# AGENTS.md

## Project shape

- All source lives in the repository root (`ejercicios/` and `tests/`).
- Teaching repo for an Algorithms & Data Structures course (Algoritmos y Estructuras de Datos - AED). Single branch `main`, no CI, no PR flow.
- Codebase is in Spanish (variable names, docstrings, docs). Keep new code/comments consistent.

## Layout

- `ejercicios/{listas_ciclos,diccionarios,archivos}.py` — **stub** functions (`pass`), 24 exercises per module (72 total) of medium-high difficulty. Replace `pass` with the implementation.
- `tests/test_{listas_ciclos,diccionarios,archivos}.py` — pytest specs. **Do not modify** — if a test fails, the bug is in your `ejercicios/` code.
- `tests/data/` — read-only CSV/text fixtures used by `test_archivos.py` (referenced as `os.path.join(os.path.dirname(__file__), "data")`).
- `pytest.ini` — already sets `-v --tb=short` and filters `DeprecationWarning`. Don't add these flags manually.
- `APUNTE.md` — course notes / reference material.
- No `pyproject.toml`, `requirements.txt`, `ruff`/`black`/`mypy`, pre-commit, or CI workflow exists. The only declared dep is `pytest` (`pip install pytest`).

## Running tests

```bash
pytest                                                                # all tests
pytest tests/test_listas_ciclos.py                                    # one module only
pytest tests/test_diccionarios.py                                     # one module only
pytest tests/test_archivos.py                                         # one module only
pytest tests/test_listas_ciclos.py::TestBuscarIndiceCaracter          # one class
```

`pytest.ini` already points `testpaths = tests`, so `pytest` with no args is the canonical full run.

## Implementing stubs

- Read the **test docstring** and the **function docstring** — together they define the spec.
- Respect immutability when a docstring specifies not mutating input lists/dicts.
- Return-type hints in docstrings are authoritative (`float`, `int`, `str`, `bool`, `list`, `dict`, `tuple`, `None`).
- Percentage and average calculations that specify rounding to 2 decimals use `round(valor, 2)`.

## Verification

Only verification in this repo is pytest. No lint, formatter, or typecheck is configured — don't invent one. After editing a stub, re-run the matching test file.
