import os
import unittest

import pytest


class DataBaseFixture:

    def __init__(self):
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)

    def create_temporary_db(self):
        raise NotImplementedError

    def create_table(self, *args, **kwargs):
        raise NotImplementedError

    def connect_db(self, db_file):
        raise NotImplementedError

    def teardown(self):
        self.session.close()
        os.remove(self.db_file)

    def check_row(self, table_name, **query):
        row = self.session.find(table_name, **query)
        assert row is not None
        ...


class DataBaseTesting(DataBaseFixture):

    def __init__(self, test_case):
        super().__init__()
        test_case.addCleanup(self.teardown)


@pytest.fixture
def db_testing():
    result = DataBaseFixture()
    yield result
    result.teardown()


class Test(unittest.TestCase):

    def test_sample(self):
        db_testing = DataBaseTesting(self)
        db_testing.create_table('weapons', name=str, type=str, dmg=int)
        db_testing.check_row('weapons', name='zweihander')
