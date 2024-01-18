import pygame
import draw
import level
import config
import assets
import main

pygame.init()


def choose(player_name):
    running = True
    while running:
        pygame.display.set_caption("SokoPy - Wybierz poziom")
        for event in pygame.event.get():
            # kończy program po zamknięciu okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    return  # powraca do menu głównego
                elif event.key == pygame.K_1:
                    main.play(level.load(1), player_name)  # uruchom poziom 1 (przekazuje załadowany poziom)
                elif event.key == pygame.K_2:
                    main.play(level.load(2), player_name)
                elif event.key == pygame.K_3:
                    main.play(level.load(3), player_name)

        draw.display.fill((0, 0, 0))  # czyści ekran
        draw.draw_text(f"Gracz: {player_name}", assets.fonts["small_text_font"], assets.colors["white"], 50, 120)
        draw.draw_text_center("Wybierz poziom", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 75)
        draw.draw_text("Wciśnij klawisz:", assets.fonts["text_font"], assets.colors["white"], 50, 150)
        draw.draw_text("0. Powrót do menu głównego", assets.fonts["text_font"], assets.colors["yellow"], 50, 200)
        draw.draw_text("1. Poziom 1", assets.fonts["text_font"], assets.colors["white"], 50, 250)
        draw.draw_text("2. Poziom 2", assets.fonts["text_font"], assets.colors["white"], 50, 300)
        draw.draw_text("3. Poziom 3", assets.fonts["text_font"], assets.colors["white"], 50, 350)
        pygame.display.update()
