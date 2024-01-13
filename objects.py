import assets
import config
import movement


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

    def move(self, x, y):
        self.x += x
        self.y += y


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
