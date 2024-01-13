import assets


def get_player_sprite(last_move):
    match last_move:
        case "right":
            player_sprite = assets.images["player_right"]
        case "left":
            player_sprite = assets.images["player_left"]
        case "up":
            player_sprite = assets.images["player_up"]
        case "down":
            player_sprite = assets.images["player_down"]
        case _:
            player_sprite = assets.images["error"]
    return player_sprite
