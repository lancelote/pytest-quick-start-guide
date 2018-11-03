import pytest


def initialize_graphics():
    pass


def supports_shaders():
    pass


def test_shaders():
    initialize_graphics()

    if not supports_shaders():
        pytest.skip('shades are not supported in this driver')
