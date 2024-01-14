import assets
import config
import movement
import collision


class Player(object):
    def __init__(self, start_x, start_y, speed):
        self.x = start_x
        self.y = start_y
        self.speed = speed
        self.image = assets.images["player_down"]

    def move(self, x, y, last_move):
        self.x += x * self.speed
        self.y += y * self.speed
        self.image = movement.get_player_sprite(last_move)


class Crate(object):
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.image = assets.images["crate"]
        self.on_goal = False

    def move(self, level, crates, x, y):
        moved = False
        if not collision.wall(level, self.x + x, self.y + y) and collision.crate(crates, self.x + x, self.y + y) is False:
            self.x += x
            self.y += y
            moved = True
        if collision.goal(level, self.x, self.y):
            self.on_goal = True
        else:
            self.on_goal = False
        return moved


def create_player(level):
    x, y = 0, 0
    for row in level:
        x = 0
        for tile in row:
            if tile == 0:
                return Player(x, y, config.speed)
            x += config.speed
        y += config.speed


def create_crates(level):
    crates = []
    x, y = 0, 0
    for row in level:
        x = 0
        for tile in row:
            if tile == 2:
                crates.append(Crate(x, y))
            x += config.speed
        y += config.speed
    return crates
