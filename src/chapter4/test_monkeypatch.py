import getpass

import pytest


def check_credentials(name, password) -> bool:
    pass


def user_login(name):
    password = getpass.getpass()
    return check_credentials(name, password)


def test_login_success(monkeypatch):
    monkeypatch.setattr(getpass, 'getpass', lambda: 'valid-pass')
    assert user_login('test-user')


class AuthenticationError(Exception):
    pass


def test_login_wrong_password(monkeypatch):
    monkeypatch.setattr(getpass, 'getpass', lambda: 'wrong-pass')
    with pytest.raises(AuthenticationError, match='wrong password'):
        user_login('test-user')
