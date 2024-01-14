import pygame
import config
import assets

pygame.display.set_caption("Pierwsza gra w Pygame")
display = pygame.display.set_mode((config.window_width, config.window_height))


def draw_text_center(text, font, text_color, x, y):
    txt = font.render(text, True, text_color)
    text_rect = txt.get_rect(center=(x, y))
    display.blit(txt, text_rect)


def draw_text(text, font, text_color, x, y):
    txt = font.render(text, True, text_color)
    display.blit(txt, (x, y))


def draw_level(level):
    display.fill((125, 125, 125))
    x, y = 0, 0
    for row in level:
        x = 0
        for tile in row:
            display.blit(assets.images["ground"], (x, y))  # rysuje podłogę
            if tile == 1:
                display.blit(assets.images["wall"], (x, y))  # rysuje ścianę
            elif tile == 3:
                display.blit(assets.images["goal"], (x, y))  # rysuje cel
            x += config.width
        y += config.height


def update(level, player, crates):
    draw_level(level)
    for crate in crates:
        display.blit(crate.image, (crate.x, crate.y))  # rysuje skrzynkę
    display.blit(player.image, (player.x, player.y))  # rysuje gracza
    pygame.display.update()
