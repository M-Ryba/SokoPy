from collision import wall, goal, crate
import level
import config


# test wykrywania kolizji ze ścianą
def test_wall():
    speed = config.speed
    lvl = level.load(1)
    assert wall(lvl, 4 * speed, 4 * speed)
    assert wall(lvl, 10 * speed, 8 * speed)
    assert wall(lvl, 7 * speed, 10 * speed)
    assert wall(lvl, 8 * speed, 4 * speed)
    lvl = level.load(2)
    print(wall(lvl, 7 * speed, 7 * speed))
    # lvl = level.load(3)
    # assert wall(lvl, 4 * speed, 9 * speed)
    # assert wall(lvl, 10 * speed, 8 * speed)
