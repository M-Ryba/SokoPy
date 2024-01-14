import pygame
import assets
import input
import leaderboards
import draw
import config
import level_menu

pygame.init()


def mainloop():
    running = True
    while running:
        pygame.display.set_caption("SokoPy")
        for event in pygame.event.get():
            # kończy program po zamknięciu okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_name = input.name()
                    level_menu.choose(player_name)
                elif event.key == pygame.K_2:
                    leaderboards.display()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    exit()

        draw.display.fill((0, 0, 0))  # czyści ekran
        draw.draw_text_center("SokoPy", assets.fonts["title_font"], assets.colors["yellow"], config.window_width // 2, 75)
        draw.draw_text("Wciśnij klawisz:", assets.fonts["text_font"], assets.colors["white"], 50, 150)
        draw.draw_text("1. Poziomy", assets.fonts["text_font"], assets.colors["white"], 50, 200)
        draw.draw_text("2. Tablica wyników", assets.fonts["text_font"], assets.colors["white"], 50, 250)
        draw.draw_text("3. Wyjdź z gry", assets.fonts["text_font"], assets.colors["white"], 50, 300)
        pygame.display.update()


mainloop()
