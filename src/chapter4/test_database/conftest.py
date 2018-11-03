import pytest


class Transaction:

    def rollback(self):
        ...

    def find(self):
        ...


class Database:

    def create_table(self, table_name):
        ...

    def disconnect(self):
        ...

    def prune(self):
        ...

    def start_transaction(self) -> Transaction:
        ...


# noinspection PyUnusedLocal
def connect_to_db(host, database) -> Database:
    ...


class Series:

    def __init__(self, name, year, ratings):
        self.name = name
        self.year = year
        self.ratings = ratings


class Actors:
    ...


@pytest.fixture(scope='session')
def db():
    db = connect_to_db('localhost', 'test')
    db.create_table(Series)
    db.create_table(Actors)
    yield db
    db.prune()
    db.disconnect()


@pytest.fixture(scope='function')
def transaction(db):
    transaction = db.start_transaction()
    yield transaction
    transaction.rollback()
