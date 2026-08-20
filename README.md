# enoppy-core

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0)
![PyPI - Version](https://img.shields.io/pypi/v/enoppy-core?style=flat-square)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/enoppy-core?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enoppy-core?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/enoppy-core?style=flat-square)
![GitHub Release Date](https://img.shields.io/github/release-date/ltsim/enoppy-core.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/enoppy-core?style=flat-square)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/publish.yml?style=flat-square&logo=pypi&label=Publish)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/test.yml?style=flat-square&logo=pytest&label=Testing)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/type.yml?style=flat-square&logo=mypy&label=Type-checking)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/lint.yml?style=flat-square&logo=ruff&label=Linting)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ltsim/enoppy-core/docs.yml?style=flat-square&logo=githubpages&label=Docs)

**A Python library for engineering optimization problems.**

This library is a fork of the [ENOPPY (ENgineering Optimization Problems in PYthon)](https://github.com/thieu1995/enoppy) library, which was originally the largest Python library for real-world engineering optimization problems. It was refactored to work with the latest versions of Python and NumPy. It contains all the real-world engineering problems from CEC competitions and research papers.

* **Free software:** GNU General Public License (GPL) V3 license
* **Total problems:** more than 50 problems
* **Documentation:** https://ltsim.github.io/enoppy-core/

## Installation

Install the [current PyPI release](https://pypi.python.org/pypi/enoppy-core):

```sh
$ pip install enoppy-core
```

or with `uv`:

```sh
$ uv add enoppy-core
```

Install from GitHub:

```sh
$ pip install git+https://github.com/ltsim/enoppy-core
```

After installation, you can import enoppy as any other Python module:

```sh
$ python
>>> import enoppy
>>> enoppy.__VERSION__
```

## Usage

This is a minimal usage example of the enoppy library.

1) Get a problem and evaluate it:

```python
from enoppy.paper_based.moeosma_2023 import SpeedReducerProblem

# SRP = SpeedReducerProblem
# SP = SpringProblem
# HTBP = HydrostaticThrustBearingProblem
# VPP = VibratingPlatformProblem
# CSP = CarSideImpactProblem
# WRMP = WaterResourceManagementProblem
# BCP = BulkCarriersProblem
# MPBPP = MultiProductBatchPlantProblem

srp_prob = SpeedReducerProblem()
print("Lower bound for this problem: ", srp_prob.lb)
print("Upper bound for this problem: ", srp_prob.ub)
x0 = srp_prob.create_solution()
print("Get the objective values of x0: ", srp_prob.get_objs(x0))
print("Get the constraint values of x0: ", srp_prob.get_cons(x0))
print("Evaluate with default penalty function: ", srp_prob.evaluate(x0))
```

2) Design your own penalty function:

```python
import numpy as np
from enoppy.paper_based.moeosma_2023 import HTBP
# HTBP = HydrostaticThrustBearingProblem


def penalty_func(list_objectives, list_constraints):
    list_constraints[list_constraints < 0] = 0
    return np.sum(list_objectives) + 1e5 * np.sum(list_constraints**2)


htbp_prob = HTBP(f_penalty=penalty_func)
print("Lower bound for this problem: ", htbp_prob.lb)
print("Upper bound for this problem: ", htbp_prob.ub)

x0 = htbp_prob.create_solution()
print("Get the objective values of x0: ", htbp_prob.get_objs(x0))
print("Get the constraint values of x0: ", htbp_prob.get_cons(x0))
print("Evaluate with default penalty function: ", htbp_prob.evaluate(x0))
```

## Development

This project uses the `uv` package manager with a `src/` layout:

```sh
$ uv sync --all-extras   # install the project and dev/docs dependencies
$ uv run pytest          # run the test suite
$ uv run ruff check .    # lint
$ uv run mypy            # type-check
$ uv run mkdocs serve    # local documentation server
```

## Acknowledgments

If you are using enoppy in your project, we would appreciate citations:

```code
@software{nguyen_van_thieu_2023_7953207,
  author       = {Nguyen Van Thieu},
  title        = {ENOPPY: A Python Library for Engineering Optimization Problems},
  year         = 2023,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.7953206},
  url          = {https://github.com/thieu1995/enoppy}
}
```

The full bibliography of the implemented problems is maintained in [`references.bib`](references.bib) and rendered in the [docs](https://ltsim.github.io/enoppy-core/references/).

---

* Maintained by: [LTSIM](mailto:tsim@cucei.udg.mx) @ 2026
* Developed by: [Thieu](mailto:nguyenthieu2102@gmail.com?Subject=Opfunu_QUESTIONS) @ 2023
