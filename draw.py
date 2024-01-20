import pygame
import config
import assets

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


def win_screen(player_name, level_number, score):
    pygame.display.set_caption("Wygrana!")
    display.fill((0, 0, 0))
    draw_text_center("Wygrana!", assets.fonts["title_font"], assets.colors["yellow"], config.window_width // 2, 300)
    draw_text_center(f"Gracz: {player_name}", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 400)
    draw_text_center(f"Poziom: {level_number}", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 500)
    draw_text_center(f"Wynik: {score}", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 600)
    draw_text_center("Wynik zapisany na liście", assets.fonts["text_font"], assets.colors["white"], config.window_width // 2, 700)
    draw_text_center("Wciśnij klawisz 0, aby wrócić do wyboru poziomów", assets.fonts["text_font"], assets.colors["blue"], config.window_width // 2, 750)
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            # kończy program po zamknięciu okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    return
