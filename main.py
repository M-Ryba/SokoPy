import pygame
import config
import leaderboards
import objects
import sound
import draw
import collision

pygame.init()


def play(level, player_name, level_number):
    pygame.display.set_caption("SokoPy - Poziom 1 (naciśnij klawisz ESCAPE, aby wyjść z poziomu)")
    walk_cooldown = 0
    # opóźnienie między ruchami
    walk_delay = 1
    speed = config.speed

    draw.draw_level(level)  # rysuje poziom
    player = objects.create_player(level)  # tworzy gracza (jeden obiekt)
    crates = objects.create_crates(level)  # tworzy skrzynki (obiekty w liście)

    clock = pygame.time.Clock()
    score = 0

    running = True
    while running:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            # kończy program po zamknięciu okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        keys = pygame.key.get_pressed()
        # zmniejszenie licznika czasu do następnego ruchu
        delta = clock.tick() / 150.0
        walk_cooldown -= delta

        if walk_cooldown <= 0:
            # jeśli strzałka w prawo jest wciśnięta i gracz nie wyjdzie poza ekran
            if keys[pygame.K_RIGHT] and (player.x + speed) < config.window_width:
                if not collision.wall(level, player.x + speed, player.y):
                    crate_index = collision.crate(crates, player.x + speed, player.y)
                    if crate_index is not False:
                        if crates[crate_index].move(level, crates, speed, 0):
                            player.move(1, 0, "right")
                            score += 1
                            sound.play_sound("crate_move")
                    else:
                        player.move(1, 0, "right")
                        score += 1
                        sound.play_sound("player_move")
                    walk_cooldown = walk_delay  # ustawia z powrotem licznik czasu do następnego ruchu
            elif keys[pygame.K_LEFT] and (player.x - speed) >= 0:  # strzałka w lewo
                if not collision.wall(level, player.x - speed, player.y):
                    crate_index = collision.crate(crates, player.x - speed, player.y)
                    if crate_index is not False:
                        # jeśli skrzynka została rzeczywiście przesunięta (nie napotkała na przeszkodę)
                        if crates[crate_index].move(level, crates, -speed, 0):
                            player.move(-1, 0, "left")
                            score += 1
                            sound.play_sound("crate_move")
                    else:
                        player.move(-1, 0, "left")
                        score += 1
                        sound.play_sound("player_move")
                    walk_cooldown = walk_delay

            elif keys[pygame.K_UP] and (player.y - speed) >= 0:  # strzałka w górę
                if not collision.wall(level, player.x, player.y - speed):
                    crate_index = collision.crate(crates, player.x, player.y - speed)
                    if crate_index is not False:
                        if crates[crate_index].move(level, crates, 0, -speed):
                            player.move(0, -1, "up")
                            score += 1
                            sound.play_sound("crate_move")
                    else:
                        player.move(0, -1, "up")
                        score += 1
                        sound.play_sound("player_move")
                    walk_cooldown = walk_delay
            elif keys[pygame.K_DOWN] and (player.y + speed) < config.window_width:  # strzałka w dół
                if not collision.wall(level, player.x, player.y + speed):
                    crate_index = collision.crate(crates, player.x, player.y + speed)
                    if crate_index is not False:
                        if crates[crate_index].move(level, crates, 0, speed):
                            player.move(0, 1, "down")
                            score += 1
                            sound.play_sound("crate_move")
                    else:
                        player.move(0, 1, "down")
                        score += 1
                        sound.play_sound("player_move")
                    walk_cooldown = walk_delay

            win = True
            for c in crates:
                if not c.on_goal:
                    win = False

            if win:
                leaderboards.add(player_name, level_number, score)
                draw.win_screen(player_name, level_number, score)
                print("Wygrana!")
                return

        draw.update(level, player, crates)

    pygame.quit()
