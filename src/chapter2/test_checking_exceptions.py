import pytest

VALID_CLASSES = ['sorcerer', 'warrior']


class InvalidCharacterNameError(Exception):
    pass


class InvalidClassNameError(Exception):
    pass


class Character:
    pass


def create_characters(name: str, class_name: str) -> Character:
    """
    Creates a new character and inserts it into the database.

    :param name: the character name.

    :param class_name: the character class name.

    :raise InvalidCharacterNameError: if the character name is empty.

    :raise InvalidClassNameError: if the class name is invalid.

    :return: the newly created Character.
    """
    if not name:
        raise InvalidCharacterNameError('character name empty')

    if class_name not in VALID_CLASSES:
        raise InvalidClassNameError(f'invalid class name: {class_name}')

    return Character()


# Checking exception #
######################


def test_empty_name():
    with pytest.raises(InvalidCharacterNameError):
        create_characters(name='', class_name='warrior')


def test_invalid_class_name():
    with pytest.raises(InvalidCharacterNameError):
        create_characters(name='Solaire', class_name='mage')


# Checking exception message #
##############################


def test_empty_name_message():
    with pytest.raises(InvalidCharacterNameError,
                       match='character name empty'):
        create_characters(name='', class_name='warrior')


def test_invalid_class_name_message():
    with pytest.raises(InvalidClassNameError,
                       match='invalid class name: "mage"'):
        create_characters(name='Solaire', class_name='mage')
