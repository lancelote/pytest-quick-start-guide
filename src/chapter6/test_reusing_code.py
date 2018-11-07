import os
import unittest

import pytest


class DataBaseFixture:

    def __init__(self, tmpdir):
        self.db_file = str(tmpdir / 'file.db')
        self.session = self.connect_db(self.db_file)

    def teardown(self):
        self.session.close()
        os.remove(self.db_file)

    def connect_db(self, file):
        raise NotImplementedError


@pytest.fixture
def db_testing(tmpdir):
    fixture = DataBaseFixture(tmpdir)
    yield fixture
    fixture.teardown()


class GUIFixture:

    def __init__(self):
        self.app = self.create_app()

    def teardown(self):
        self.app.close_all_windows()

    def mouse_click(self, window, button):
        raise NotImplementedError

    def enter_text(self, window, text):
        raise NotImplementedError

    def create_app(self):
        raise NotImplementedError


@pytest.fixture
def gui_testing():
    fixture = GUIFixture()
    yield fixture
    fixture.teardown()


class DataBaseTesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _setup(self, db_testing):
        self._db_testing = db_testing

    def connect_db(self, db_file):
        return self._db_testing.connect_db(db_file)


class GUITesting(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _setup(self, gui_testing):
        self._gui_testing = gui_testing

    def mouse_click(self, window, button):
        return self._gui_testing.mouse_click(window, button)
