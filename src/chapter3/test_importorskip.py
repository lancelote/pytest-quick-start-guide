import pytest


def test_tracers_as_arrays_manual():
    try:
        import numpy
    except ImportError:
        pytest.skip('requires numpy')


def test_tracers_as_arrays():
    numpy = pytest.importorskip('numpy', minversion='1.14')
    print(numpy)
