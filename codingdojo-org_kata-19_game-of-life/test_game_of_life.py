#!/usr/bin/python3

import pytest

from game_of_life import *


def test_game_of_life_snapshot_constructor():
    game_of_life_obj = Game_of_Life_Snapshot(4, 8, 4, [[0, 0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0, 0]])
    assert game_of_life_obj.generation == 4
    assert game_of_life_obj.x_dim == 8
    assert game_of_life_obj.y_dim == 4
    assert game_of_life_obj.cellgrid == ((0, 0, 0, 0, 0, 0, 0, 0),
                                         (0, 0, 0, 0, 0, 0, 0, 0),
                                         (0, 0, 0, 0, 0, 0, 0, 0),
                                         (0, 0, 0, 0, 0, 0, 0, 0))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(-4, 2, 2, ((0, 0), (0, 0)))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(4, -2, 2, ((0, 0), (0, 0)))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(4, 2, -2, ((0, 0), (0, 0)))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(4, 1, 2, ((0, 0), (0, 0)))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(4, 2, 1, ((0, 0), (0, 0)))
    with pytest.raises(ValueError):
        game_of_life_obj = Game_of_Life_Snapshot(4, 2, 1, ({0:0, 0:0}, (0, 0)))


def test_game_of_life_snapshot_advance():
    game_of_life_obj = Game_of_Life_Snapshot(4, 8, 4, [[0, 0, 0, 1, 0, 0, 0, 0],
                                                       [0, 0, 0, 0, 1, 0, 0, 0],
                                                       [0, 0, 1, 1, 1, 0, 0, 0],
                                                       [0, 0, 0, 0, 0, 0, 0, 0]])
    game_of_life_obj.advance()
    assert game_of_life_obj.cellgrid == ((0, 0, 0, 0, 0, 0, 0, 0),
                                         (0, 0, 1, 0, 1, 0, 0, 0),
                                         (0, 0, 0, 1, 1, 0, 0, 0),
                                         (0, 0, 0, 1, 0, 0, 0, 0))


def test_parse_snapshot_file():
    input_text1 = """
Generation 4:
8 4
........
....*...
...**...
........
"""
    snapshot_obj1 = parse_snapshot_file(input_text1)
    assert snapshot_obj1.generation == 4
    assert snapshot_obj1.x_dim == 8
    assert snapshot_obj1.y_dim == 4
    assert snapshot_obj1.cellgrid == ((0, 0, 0, 0, 0, 0, 0, 0),
                                      (0, 0, 0, 0, 1, 0, 0, 0),
                                      (0, 0, 0, 1, 1, 0, 0, 0),
                                      (0, 0, 0, 0, 0, 0, 0, 0))

    with pytest.raises(ParsingError):
        input_text2 = """
Generation 4
8 4
........
....*...
...**...
........
"""
        snapshot_obj2 = parse_snapshot_file(input_text2)

    with pytest.raises(ParsingError):
        input_text3 = """
Generation 4:
8, 4
........
....*...
...**...
........
"""
        snapshot_obj3 = parse_snapshot_file(input_text3)

    with pytest.raises(ParsingError):
        input_text4 = """
Generation 4:
8, 4
........
....*...
...**...
........
"""
        snapshot_obj4 = parse_snapshot_file(input_text4)

    with pytest.raises(ParsingError):
        input_text5 = """
Generation 4:
8, 4
........
....*...
...**...
"""
        snapshot_obj5 = parse_snapshot_file(input_text5)

    with pytest.raises(ParsingError):
        input_text6 = """
Generation 4:
8, 4
.......
....*..
...**..
.......
"""
        snapshot_obj6 = parse_snapshot_file(input_text6)

