import locale

import pytest


@pytest.fixture(autouse=True)
def setup_locale(request):
    mark = request.node.get_closest_marker('change_locale')
    loc = mark.args[0] if mark is not None else 'en_US'
    locale.setlocale(locale.LC_ALL, loc)
    yield
    locale.setlocale(locale.LC_ALL, None)


@pytest.mark.change_locale('pt_BR')
def test_currency_us():
    assert locale.currency(10.5) == '$10.50'
