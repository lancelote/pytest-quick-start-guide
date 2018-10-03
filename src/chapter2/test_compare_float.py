import numpy as np
from pytest import approx


# Basic Approach #
##################


def test_simple_math():
    assert abs(0.1 + 0.2) - 0.3 < 0.0001


# With approx #
###############


def test_approx_simple():
    assert 0.1 + 0.2 == approx(0.3)


# Use for lists #
#################


def test_approx_list():
    assert [0.1 + 1.2, 0.2 + 0.8] == approx([1.3, 1.0])


# Use for dicts #
#################


def test_approx_dict():
    values = {'v1': 0.1 + 1.2, 'v2': 0.2 + 0.8}
    assert values == approx(dict(v1=1.3, v2=1.0))


# numpy arrays #
################


def test_approx_numpy():
    values = np.array([0.1, 0.2]) + np.array([1.2, 0.8])
    assert values == approx(np.array([1.3, 1.0]))


# nice fail error #
###################


def test_approx_simple_fail():
    assert 0.1 + 0.2 == approx(0.35)
