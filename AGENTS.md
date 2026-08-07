# AGENTS.md

## Project shape

- Git repo root contains **no Python code**. All source lives in the `fundamentos-python/` subdirectory.
- Teaching repo for a Python fundamentals course (Algoritmos y Programación). Single branch `main`, no CI, no PR flow, remote is `jblancoetec/ayp-fundamentos-python`.
- Codebase is in Spanish (variable names, docstrings, docs). Keep new code/comments consistent.

## Layout (`fundamentos-python/`)

- `ejercicios/{variables,condicionales,funciones,archivos_listas}.py` — **stub** functions (`pass`). Replace `pass` with the implementation.
- `tests/test_*.py` — pytest specs. **Do not modify** — if a test fails, the bug is in your `ejercicios/` code.
- `tests/data/` — read-only CSV/text fixtures used by `test_archivos_listas.py` (referenced as `os.path.join(os.path.dirname(__file__), "data")`).
- `pytest.ini` — already sets `-v --tb=short` and filters `DeprecationWarning`. Don't add these flags manually.
- `APUNTE.md` — course notes / reference material.
- No `pyproject.toml`, `requirements.txt`, `ruff`/`black`/`mypy`, pre-commit, or CI workflow exists. The only declared dep is `pytest` (`pip install pytest`).

## Running tests

Tests do `sys.path.insert(0, "../ejercicios")` **and** `from ejercicios.variables import …`. Both forms only resolve when pytest's CWD is `fundamentos-python/`. Running from the repo root will fail to import.

```bash
cd fundamentos-python
pytest                              # all tests
pytest tests/test_variables.py      # one module only
pytest tests/test_funciones.py::TestSumar::test_suma_positivos   # one test
pytest tests/test_archivos_listas.py::TestContarLineas            # one class
```

`pytest.ini` already points `testpaths = tests`, so `pytest` with no args is the canonical full run.

## Implementing stubs

- Read the **test docstring** first — it is the spec. Function docstrings in `ejercicios/` repeat it.
- Some exercises don't `return`: they set module-level globals (e.g. `crear_variables_primitivas` in `ejercicios/variables.py:6`) or `print` (e.g. `saludar` in `ejercicios/funciones.py:6`). Match what the test asserts, not just what the docstring says.
- Return-type hints in docstrings are authoritative (`float`, `int`, `str`, `bool`). For example `sumar_dos_numeros` returns `float` even for integer inputs.
- `calcular_imc` requires rounding to 2 decimals — the test compares floats exactly, not approximately.

## Verification

Only verification in this repo is pytest. No lint, formatter, or typecheck is configured — don't invent one. After editing a stub, re-run the matching test file.
