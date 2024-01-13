import pygame
import config
import assets

pygame.display.set_caption("Pierwsza gra w Pygame")
window = pygame.display.set_mode((config.window_width, config.window_height))


def draw_level(level):
    window.fill((125, 125, 125))
    x, y = 0, 0
    for row in level:
        x = 0
        for tile in row:
            window.blit(assets.images["ground"], (x, y))  # rysuje podłogę
            if tile == 1:
                window.blit(assets.images["wall"], (x, y))  # rysuje ścianę
            elif tile == 3:
                window.blit(assets.images["goal"], (x, y))  # rysuje cel
            x += config.width
        y += config.height


def update(level, player, crates):
    draw_level(level)
    for crate in crates:
        window.blit(crate.image, (crate.x, crate.y))  # rysuje skrzynkę
    window.blit(player.image, (player.x, player.y))  # rysuje gracza
    pygame.display.update()
