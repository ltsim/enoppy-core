# ENOPPY (Core)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7953206.svg)](https://doi.org/10.5281/zenodo.7953206)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This library is a fork of the [ENOPPY](https://github.com/thieu1995/enoppy) library, which was originally the largest Python library for real-world engineering optimization problems. It was refactored to work with the latest versions of Python and NumPy. It contains all the real-world engineering problems from CEC competitions and research papers.

* **Free software:** GNU General Public License (GPL) V3 license
* **Total problems**: > 50 problems
* **Python versions:** 3.10.x, 3.11.x, 3.12.x, 3.13.x, 3.14.x
* **Dependencies:** numpy, scipy

# Installation

Install the [current PyPI release](https://pypi.python.org/pypi/enoppy):
```sh 
$ pip install git+https://github.com/ltsim/enoppy-core
```

After installation, you can import ENOPPY as any other Python module:

```sh
$ python
>>> import enoppy
>>> enoppy.__version__
```


# Usage

This is a minimal usage example of the enoppy library.

1) How to get the problem and use it

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

2) Design my own penalty function:

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

# Acknowledgments

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

@article{van2023mealpy,
  title={MEALPY: An open-source library for latest meta-heuristic algorithms in Python},
  author={Van Thieu, Nguyen and Mirjalili, Seyedali},
  journal={Journal of Systems Architecture},
  year={2023},
  publisher={Elsevier},
  doi={10.1016/j.sysarc.2023.102871}
}
```

## References 

#### paper_based

* **ihaoavoa_2022**: Xiao, Y., Guo, Y., Cui, H., Wang, Y., Li, J., & Zhang, Y. (2022). IHAOAVOA: An improved hybrid aquila optimizer and African vultures optimization algorithm for global optimization problems. Mathematical Biosciences and Engineering, 19(11), 10963-11017.

* **moeosma_2023**: Luo, Q., Yin, S., Zhou, G., Meng, W., Zhao, Y., & Zhou, Y. (2023). Multi-objective equilibrium optimizer slime mould algorithm and its application in solving engineering problems. Structural and Multidisciplinary Optimization, 66(5), 114.

* **pdo_2022**: Ezugwu, A. E., Agushaka, J. O., Abualigah, L., Mirjalili, S., & Gandomi, A. H. (2022). Prairie dog optimization algorithm. Neural Computing and Applications, 34(22), 20017-20065.

* **rwco_2020**: Kumar, A., Wu, G., Ali, M. Z., Mallipeddi, R., Suganthan, P. N., & Das, S. (2020). A test-suite of non-convex constrained optimization problems from the real-world and some baseline results. Swarm and Evolutionary Computation, 56, 100693.
