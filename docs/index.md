---
title: enoppy-core
hide:
  - navigation
  - toc
---

<div align="center" markdown>

# enoppy-core

**A Python library for engineering optimization problems.**

[![PyPI - Version](https://img.shields.io/pypi/v/enoppy-core?style=flat-square)](https://pypi.org/project/enoppy-core/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/enoppy-core?style=flat-square)](https://pypi.org/project/enoppy-core/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enoppy-core?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/enoppy-core?style=flat-square)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0)
[![Docs](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/docs.yml?style=flat-square&logo=githubpages&label=Docs)](https://ltsim.github.io/enoppy-core/)
[![Testing](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/test.yml?style=flat-square&logo=pytest&label=Testing)](https://github.com/ltsim/enoppy-core/actions)

</div>

<div class="grid cards" markdown>

-   :material-engine: **50+ engineering problems**

    Real-world design problems from CEC competitions and research papers,
    from speed reducers to heat exchanger networks.

-   :material-file-document-outline: **Faithful to the papers**

    Each problem implements the objectives, constraints and bounds exactly
    as published, with the full bibliography in `references.bib`.

-   :material-code-json: **One simple API**

    Every problem shares the same `Engineer` interface: bounds, solution
    creation, objectives, constraints and evaluation.

-   :material-cog: **Built on NumPy & SciPy**

    Lightweight, vectorised and compatible with the latest Python and
    NumPy versions.

</div>

## Installation

```sh
$ pip install enoppy-core
```

or with `uv`:

```sh
$ uv add enoppy-core
```

or directly from GitHub:

```sh
$ pip install git+https://github.com/ltsim/enoppy-core
```

Then import it as any other module:

```sh
$ python
>>> import enoppy
>>> enoppy.__VERSION__
```

## Quickstart

```python
from enoppy.paper_based.moeosma_2023 import SpeedReducerProblem

srp_prob = SpeedReducerProblem()
print("Lower bound for this problem: ", srp_prob.lb)
print("Upper bound for this problem: ", srp_prob.ub)
x0 = srp_prob.create_solution()
print("Get the objective values of x0: ", srp_prob.get_objs(x0))
print("Get the constraint values of x0: ", srp_prob.get_cons(x0))
print("Evaluate with default penalty function: ", srp_prob.evaluate(x0))
```

<div class="grid cards" markdown>

-   [**Usage guide** :octicons-arrow-right-24:](usage.md)

    More examples, including custom penalty functions.

-   [**API reference** :octicons-arrow-right-24:](api/index.md)

    Every module, class and method, kept separate and searchable.

-   [**References** :octicons-arrow-right-24:](references.md)

    The papers behind the problems and how to cite this library.

</div>
