import config


def wall(level, x, y):
    if level[x // config.speed][y // config.speed] == 1:
        return True
    else:
        return False


def goal(level, x, y):
    if level[y // config.speed][x // config.speed] == 3:  # z jakiegoś powodu x i y śą odwrócone (do sprawdzenia)
        return True
    else:
        return False


def crate(crates, x, y):
    for c in range(0, len(crates)):
        if (crates[c].x == x) and (crates[c].y == y):
            return c
    return False
