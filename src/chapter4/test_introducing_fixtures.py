from operator import itemgetter

import pytest


@pytest.fixture
def comedy_series():
    return [
        ('The Office', 2005, 8.8),
        ('Scrubs', 2001, 8.4),
        ('IT Crowd', 2006, 8.5),
        ('Parks and Recreations', 2009, 8.6),
        ('Seinfeld', 1989, 8.9)
    ]


def highest_rated(series):
    return max(series, key=itemgetter(2))[0]


def oldest(series):
    return min(series, key=itemgetter(1))[0]


def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == 'Seinfeld'


def test_oldest(comedy_series):
    assert oldest(comedy_series) == 'Seinfeld'


class Test:

    @pytest.fixture
    def drama_series(self):
        return [
            ('The Mentalist', 2008, 8.1),
            ('Game of Thrones', 2011, 9.5),
            ('The Newsroom', 2012, 8.6),
            ('Cosmos', 1980, 9.3)
        ]

    def test_highest_rated(self, drama_series):
        assert highest_rated(drama_series) == 'Game of Thrones'

    def test_oldest(self, drama_series):
        assert oldest(drama_series) == 'Cosmos'
