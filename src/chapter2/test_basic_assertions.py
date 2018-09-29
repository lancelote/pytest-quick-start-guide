import textwrap


# Basic assert #
################


def get_default_health(class_name):
    assert class_name == "warrior"
    return 80


def test_default_health():
    health = get_default_health('warrior')
    assert health == 95


# Text differences #
####################


def get_default_player_class():
    return "warrior"


def test_default_player_class():
    x = get_default_player_class()
    assert x == 'sorcerer'


def get_short_class_description(class_name):
    assert class_name == "warrior"
    return "A battle-hardened veteran, favors heavy armor and weapons."


def test_warrior_short_description():
    desc = get_short_class_description('warrior')
    assert desc == 'A battle-hardened veteran, can equip heavy armor and ' \
                   'weapons.'


def get_long_class_description(class_name):
    assert class_name == "warrior"
    return textwrap.dedent("""\
        A seasoned veteran of many battles. High Strength and Dexterity
        allow to yield heavy armor and weapons, as well as carry
        more equipment while keeping a light roll. Weak in magic.            
        """)


def test_warrior_long_description():
    desc = get_long_class_description('warrior')
    assert desc == textwrap.dedent("""\
        A seasoned veteran of many battles. Strength and Dexterity
        allow to yield heavy armor and weapons, as well as carry
        more equipment. Weak in magic.
        """)


# Lists #
#########


def get_starting_equipment(class_name):
    assert class_name == "warrior"
    return ["long sword", "warrior set", "shield"]


def test_get_starting_equipment():
    expected = ['long sword', 'shield']
    assert get_starting_equipment('warrior') == expected


# Dictionaries and sets #
#########################


def get_classes_starting_health():
    return {"warrior": 85, "sorcerer": 55, "knight": 95}


def test_starting_health():
    expected = {'warrior': 85, 'sorcerer': 50}
    assert get_classes_starting_health() == expected


def get_player_classes():
    return {"warrior", "knight", "sorcerer"}


def test_player_classes():
    assert get_player_classes() == {'warrior', 'sorcerer'}
