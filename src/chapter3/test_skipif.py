import os
import sys

import pytest


@pytest.mark.skipif(
    sys.platform.startswith('win'),
    reason='fork not available on Windows',
)
def test_spawn_server_using_fork():
    pass


@pytest.mark.skipif(
    not hasattr(os, 'fork'),
    reason='os.fork is not available'
)
def test_spawn_server_using_fork2():
    pass
