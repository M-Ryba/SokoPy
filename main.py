import pygame
import config
import objects
import sound
import draw

pygame.init()


def play(level):
    walk_cooldown = 0
    # opóźnienie między ruchami
    walk_delay = 1

    draw.draw_level(level)  # rysuje poziom
    player = objects.create_player(level)  # tworzy gracza (jeden obiekt)
    crates = objects.create_crates(level)  # tworzy skrzynki (obiekty w liście)

    clock = pygame.time.Clock()

    running = True
    while running:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            # kończy program po zamknięciu okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        # zmniejszenie licznika czasu do następnego ruchu
        delta = clock.tick() / 150.0
        walk_cooldown -= delta

        if walk_cooldown <= 0:
            # jeśli strzałka w prawo jest wciśnięta i gracz nie wyjdzie poza ekran
            if keys[pygame.K_RIGHT] and (player.x + config.speed) < config.window_width:
                walk_cooldown = walk_delay  # ustawia z powrotem licznik czasu do następnego ruchu
                player.move(1, 0, "right")
                sound.play_sound("player_move")
            elif keys[pygame.K_LEFT] and (player.x - config.speed) >= 0:  # strzałka w lewo
                walk_cooldown = walk_delay
                player.move(-1, 0, "left")
                sound.play_sound("player_move")
            elif keys[pygame.K_UP] and (player.y - config.speed) >= 0:  # strzałka w górę
                walk_cooldown = walk_delay
                player.move(0, -1, "up")
                sound.play_sound("player_move")
            elif keys[pygame.K_DOWN] and (player.y + config.speed) < config.window_width:  # strzałka w dół
                walk_cooldown = walk_delay
                player.move(0, 1, "down")
                sound.play_sound("player_move")

        draw.update(level, player, crates)

    pygame.quit()
