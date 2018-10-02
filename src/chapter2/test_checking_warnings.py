import warnings
from enum import Enum
from typing import Union

import pytest


def get_initial_hit_points(player_class: str) -> int:
    """
    Return the initial hit points of the given class.
    :param player_class: player class name.
    """
    return 1 if player_class == 'warrior' else 0


class PlayerClass(Enum):
    WARRIOR = 1
    KNIGHT = 2
    SORCERER = 3
    CLERIC = 4


HITPOINTS = {
    PlayerClass.WARRIOR: 42,
    PlayerClass.KNIGHT: 30,
    PlayerClass.SORCERER: 20,
    PlayerClass.CLERIC: 10
}


def get_player_enum_from_string(player_class):
    return {
        "warrior": PlayerClass.WARRIOR,
        "knight": PlayerClass.KNIGHT,
        "sorcerer": PlayerClass.SORCERER,
        "cleric": PlayerClass.CLERIC,
    }[player_class]


def get_initial_hit_points_new(player_class: Union[PlayerClass, str]) -> int:
    if isinstance(player_class, str):
        msg = "Using player_class as str has been deprecated "\
              "and will be removed in the future"
        warnings.warn(DeprecationWarning(msg))
        player_class = get_player_enum_from_string(player_class)
    return HITPOINTS[player_class]


def test_get_initial_hit_points_warning():
    with pytest.warns(DeprecationWarning):
        get_initial_hit_points_new('warrior')


def test_get_initial_hit_points_warning_message():
    with pytest.warns(DeprecationWarning,
                      match='.*str has been deprecated.*'):
        get_initial_hit_points_new('warrior')
