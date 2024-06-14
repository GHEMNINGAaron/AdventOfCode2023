import pytest

from Day2.cube_game.cube_game import (transform_game_in_dictionary, verifiy_numbers_of_cube,
                                      sum_of_id_of_possible_games, fewest_number_of_cubes, sum_of_power_of_a_set_of_games)
def test_transform_string_in_dictionary():
    assert transform_game_in_dictionary("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}
    assert transform_game_in_dictionary('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == {2: [{'blue': 1, 'green': 2}, {'green': 3, 'blue': 4, 'red': 1}, {'green': 1, 'blue': 1}]}


def test_verify_numbers_of_cube():
    assert verifiy_numbers_of_cube({1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}) == True
    assert verifiy_numbers_of_cube({4: [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}]}) == False


def test_sum_of_id_of_possible_games():
    assert sum_of_id_of_possible_games(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                                        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                                        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                                        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                                        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]) == 8


def test_fewest_number_of_cubes():
    assert fewest_number_of_cubes({1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}) == {"blue":6, "red":4, "green":2}
    assert fewest_number_of_cubes({4: [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}]}) == {"red":14, "green":3, "blue":15}


def test_sum_of_power_of_a_set_of_games():
    assert sum_of_power_of_a_set_of_games(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                                           "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                                           "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                                           "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                                           "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]) == 2286