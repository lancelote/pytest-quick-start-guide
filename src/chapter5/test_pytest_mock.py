import getpass


def user_login(user):
    password = getpass.getpass('enter password: ')


def test_login_success(mocker):
    mocked = mocker.patch.object(getpass, 'getpass', return_value='valid-pass')
    assert user_login('test-user')
    mocked.assert_called_with('enter password: ')
