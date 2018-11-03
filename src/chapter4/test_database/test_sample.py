from chapter4.test_database.conftest import Series


def test_insert(transaction):
    transaction.add(Series('The Office', 2005, 8.8))
    assert transaction.find(name='The Office') is not None
