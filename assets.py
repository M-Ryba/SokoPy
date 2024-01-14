import pygame
pygame.init()

images = {
    "player_right": pygame.image.load("assets/images/player_right.png"),
    "player_left": pygame.image.load("assets/images/player_left.png"),
    "player_up": pygame.image.load("assets/images/player_up.png"),
    "player_down": pygame.image.load("assets/images/player_down.png"),
    "crate": pygame.image.load("assets/images/crate.png"),
    "wall": pygame.image.load("assets/images/wall.png"),
    "ground": pygame.image.load("assets/images/ground.png"),
    "goal": pygame.image.load("assets/images/goal.png"),
    "error": pygame.image.load("assets/images/error.png")
}

sounds = {
    "menu": pygame.mixer.Sound("assets/sounds/menu.ogg"),
    "crate_on_goal": pygame.mixer.Sound("assets/sounds/create_on_goal.ogg"),
    "crate_move": pygame.mixer.Sound("assets/sounds/crate_move.ogg"),
    "level_finished": pygame.mixer.Sound("assets/sounds/level_finished.ogg"),
    "error": pygame.mixer.Sound("assets/sounds/error.ogg"),
    "player_move": pygame.mixer.Sound("assets/sounds/player_move.ogg")
}

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0)
}

fonts = {
    "title_font": pygame.font.SysFont("arialblack", 70),
    "text_font": pygame.font.SysFont("arialblack", 30),
    "small_text_font": pygame.font.SysFont("arialblack", 20)
}