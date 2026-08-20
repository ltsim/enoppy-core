# Version 2026a

+ Migrate to the `uv` package structure with a `src/` layout
+ Switch to the hatchling build backend; version now sourced from `__VERSION__` in `src/enoppy/__init__.py`
+ Add Ruff configuration (replacing flake8) and a lint workflow
+ Add pytest and mypy configuration in `pyproject.toml`
+ Migrate GitHub Actions workflows to `uv` and add a docs (GitHub Pages) workflow
+ Move documentation to MkDocs with the Material theme, `mkdocstrings` API reference, and `.bib` citations via `mkdocs-bibtex`
+ Refactor `README.md` and remove the legacy Sphinx/ReadTheDocs configuration

---------------------------------------------------------------------

# Version 0.1.2.1

+ Updating dependencies such as NumPy and SciPy
+ Removing unnecessary external dependencies
+ Partial support for PyPy 3.11

---------------------------------------------------------------------

# Version 0.1.1

+ Add docs
+ Add tests
+ Add citation
+ Add Github Action
+ Add engineering problems from papers:
  + Prairie Dog Optimization Algorithm (pdo_2022)
  + A Test-suite of Non-Convex Constrained Optimization Problems from the Real-World and Some Baseline Results (rwco_2020)


---------------------------------------------------------------------

# Version 0.1.0 (First version)

+ Add project, Engineer class, utils module.
+ Add engineering problems from papers:
  + Multi‑objective equilibrium optimizer slime mould algorithm and its application in solving engineering problems (moeosma_2023)
  + IHAOAVOA: An improved hybrid aquila optimizer and African vultures optimization algorithm for global optimization problems (ihaoavoa_2022)

