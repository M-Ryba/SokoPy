import pygame
import assets
import draw
import config
import json
import algorithms


def load():
    try:
        leaderboard = json.load(open("assets/leaderboard.json", "r"))
        return leaderboard
    except:
        # tworzy plik leaderboard.json z gotową strukturą lub nadpisuje istniejący z błędem
        leaderboard = {"1": [], "2": [], "3": []}
        json.dump(leaderboard, open("assets/leaderboard.json", 'w'))
        return leaderboard


def add(player_name, level_number, score):
    leaderboard = load()
    level_scores = leaderboard[str(level_number)]
    player_exists = False
    player_index = 0
    for i in range(0, len(level_scores)):
        # jeśli nazwa gracza już istnieje w jednej z krotek
        if player_name in level_scores[i]:
            player_exists = True
            player_index = i
            break
    if not player_exists:
        level_scores.append((player_name, score))
    elif player_exists:
        if score < level_scores[player_index][1]:
            level_scores.pop(player_index)
            level_scores.append((player_name, score))
    leaderboard_sorted = algorithms.sort_leaderboard(leaderboard)
    json.dump(leaderboard_sorted, open("assets/leaderboard.json", 'w'))


def display():
    leaderboard = load()
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
