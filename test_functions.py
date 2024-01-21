from collision import wall, goal
from algorithms import sort_leaderboard
from level import load
from movement import get_player_sprite
import config
import assets


# test ładowania poziomów z pliku
def test_load():
    level1 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, -1, 2, 0, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 3, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 3, 1, 2, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    level2 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, 3, 1, 3, 1, -1, -1, -1, -1, -1], [-1, -1, -1, 1, 1, 1, -1, 2, -1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, 1, 3, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 2, -1, 2, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, 0, -1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    level3 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 0, 1, 3, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, 1, 2, 3, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 2, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 3, -1, 2, 3, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 2, -1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    assert load(1) == level1
    assert load(2) == level2
    assert load(3) == level3


# test wykrywania kolizji ze ścianą
def test_wall():
    speed = config.speed
    level1 = load(1)
    assert wall(level1, 4 * speed, 4 * speed)
    assert wall(level1, 10 * speed, 8 * speed)
    assert wall(level1, 7 * speed, 10 * speed)
    assert wall(level1, 8 * speed, 4 * speed)
    level2 = load(2)
    assert wall(level2, 8 * speed, 10 * speed)
    assert wall(level2, 6 * speed, 10 * speed)
    level3 = load(3)
    assert wall(level3, 4 * speed, 9 * speed)
    assert wall(level3, 10 * speed, 8 * speed)


def test_goal():
    speed = config.speed
    level1 = load(1)
    assert goal(level1, 6 * speed, 7 * speed)
    assert goal(level1, 6 * speed, 8 * speed)
    level2 = load(2)
    assert goal(level2, 6 * speed, 4 * speed)
    assert goal(level2, 8 * speed, 4 * speed)
    assert goal(level2, 4 * speed, 6 * speed)
    level3 = load(3)
    assert goal(level3, 9 * speed, 5 * speed)
    assert goal(level3, 8 * speed, 6 * speed)
    assert goal(level3, 6 * speed, 8 * speed)
    assert goal(level3, 9 * speed, 8 * speed)


# test sortowania listy wyników
def test_sort_leaderboard():
    leaderboard = {"1": [("Jan", 14), ("Adam", 12), ("Janusz", 23)], "2": [("Jan", 22), ("Adam", 1), ("Janusz", 14)], "3": [("Adam", 22), ("Janusz", 99)]}
    leaderboard_sorted_1 = {"1": [("Adam", 12), ("Jan", 14), ("Janusz", 23)], "2": [("Jan", 22), ("Adam", 1), ("Janusz", 14)], "3": [("Adam", 22), ("Janusz", 99)]}
    assert sort_leaderboard(leaderboard, 1) == leaderboard_sorted_1  # sortuje tablicę wyników dla 1 poziomu
    leaderboard_sorted_2 = {"1": [("Adam", 12), ("Jan", 14), ("Janusz", 23)], "2": [("Adam", 1), ("Janusz", 14), ("Jan", 22)], "3": [("Adam", 22), ("Janusz", 99)]}
    assert sort_leaderboard(leaderboard, 2) == leaderboard_sorted_2  # sortuje tablicę wyników dla 2 poziomu
    leaderboard_sorted_3 = {"1": [("Adam", 12), ("Jan", 14), ("Janusz", 23)], "2": [("Adam", 1), ("Janusz", 14), ("Jan", 22)], "3": [("Adam", 22), ("Janusz", 99)]}
    assert sort_leaderboard(leaderboard, 3) == leaderboard_sorted_3  # sortuje tablicę wyników dla 3 poziomu


def test_get_player_sprite():
    assert get_player_sprite("right") == assets.images["player_right"]
    assert get_player_sprite("left") == assets.images["player_left"]
    assert get_player_sprite("up") == assets.images["player_up"]
    assert get_player_sprite("down") == assets.images["player_down"]
    assert get_player_sprite("fdgg") == assets.images["error"]
    assert get_player_sprite("1") == assets.images["error"]
    assert get_player_sprite("") == assets.images["error"]
