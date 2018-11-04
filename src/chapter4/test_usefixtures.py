import os
import tempfile

import pytest


@pytest.fixture
def venv_dir():
    import venv

    with tempfile.TemporaryDirectory() as d:
        venv.create(d)
        pwd = os.getcwd()
        os.chdir(d)
        yield d
        os.chdir(pwd)


@pytest.mark.usefixtures('venv_dir')
class TestVirtualEnv:
    ...


@pytest.mark.usefixtures('venv_dir', 'config_python_debug')
class Test:
    ...
