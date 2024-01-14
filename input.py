import pygame
import draw
import assets
import config


def name():
    draw.display.fill((0, 0, 0))  # czyści ekran
    draw.draw_text_center("Podaj nazwę gracza:", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 50)
    pygame.display.update()
    player_name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return player_name
                else:
                    player_name += event.unicode
                    draw.draw_text(player_name, assets.fonts["text_font"], assets.colors["red"], 50, 100)
                    pygame.display.update()
