import pytest


class Window:
    def title(self) -> str:
        raise NotImplementedError


class WindowManager:

    def __init__(self, logging_directory):
        self.logging_directory = logging_directory

    def new_help_window(self, file) -> Window:
        raise NotImplementedError

    def close(self):
        """Close the WindowsManager and all associated resources."""
        raise NotImplementedError


@pytest.fixture
def manager(tmpdir):
    wm = WindowManager(str(tmpdir))
    yield wm
    wm.close()


def test_windows_creation(manager):
    window = manager.new_help_window('pipes_help.rst')
    assert window.title() == 'Pipe Setup Help'
