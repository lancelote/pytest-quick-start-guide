import pytest


@pytest.mark.slow
def test_long_computation():
    pass


@pytest.mark.timeout(10, method='thread')
def test_topology_sort():
    pass


@pytest.mark.slow
@pytest.mark.timeout(10, method='thread')
def test_topology_sort_slow():
    pass


timeout10 = pytest.mark.timeout(10, method='thread')


@timeout10
def test_topology_sort_deco():
    pass


@timeout10
def test_remove_duplicate_point():
    pass


@timeout10
class TestCase:

    def test_simple_simulation(self):
        pass

    def test_compute_tracers(self):
        pass


# To apply a mark to a module
pytestmark = [pytest.mark.slow, pytest.mark.timeout(10)]
