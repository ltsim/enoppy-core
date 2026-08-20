# Usage

Every problem in enoppy shares the same `Engineer` interface. You pick a
problem class (see the [API reference](api/index.md)), instantiate it, and
evaluate candidate solutions.

## 1. Get a problem and evaluate it

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

## 2. Design your own penalty function

By default, enoppy combines objectives and constraints with a built-in
penalty. You can plug in your own by passing `f_penalty` to the constructor:

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

## Where to go next

* [API reference](api/index.md) — every module, class and method.
* [References](references.md) — the papers behind the problems and citation info.
