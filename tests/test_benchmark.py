#!/usr/bin/env python
# Created by "Thieu" at 20:21, 30/06/2022 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%
"""Tests for the Engineer base class."""

import numpy as np

from enoppy.engineer import Engineer


class _Engineer(Engineer):
    def evaluate(self, x):
        """Evaluate the candidate solution."""
        return self.get_objs(x)


def test_Benchmark_class():
    """Test the bounds and solution properties of the Engineer base class."""
    ndim = 10
    bounds = np.array(
        [
            [
                -15,
            ]
            * ndim,
            [
                15,
            ]
            * ndim,
        ]
    ).T
    problem = _Engineer()
    problem._bounds = bounds

    x = np.random.uniform(problem.lb, problem.ub)

    assert len(problem.lb) == len(x)
    assert isinstance(problem.lb, np.ndarray)
    assert isinstance(problem.bounds, np.ndarray)
    assert problem.bounds.shape[0] == ndim
