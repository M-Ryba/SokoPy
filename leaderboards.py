import pygame
import assets
import draw
import config

leaderboard = {
    # poziom 1
    1: [("Anonim", 12), ("Jan", 9)],
    # poziom 2
    2: [("Anonim", 24)]
}


def display():
    pygame.display.set_caption("SokoPy - Tablica wyników")
    draw.display.fill((0, 0, 0))  # czyści ekran
    draw.draw_text_center("Tablica wyników", assets.fonts["title_font"], assets.colors["white"], config.window_width // 2, 75)
    draw.draw_text("Wciśnij klawisz:", assets.fonts["text_font"], assets.colors["white"], 50, 150)
    draw.draw_text("0. Powrót do menu głównego", assets.fonts["text_font"], assets.colors["white"], 50, 200)

    y = 200
    for level, scores in leaderboard.items():
        y += 50
        draw.draw_text(f"Poziom {level}:", assets.fonts["small_text_font"], assets.colors["white"], 50, y)
        for player in scores:
            y += 50
            draw.draw_text(f"{player[0]}: {player[1]} ruchów", assets.fonts["small_text_font"], assets.colors["white"], 75, y)

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
