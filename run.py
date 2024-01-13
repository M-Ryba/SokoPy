import pygame

import config
import movement
import sound
import assets
import level

pygame.init()
window = pygame.display.set_mode((config.window_width, config.window_height))
pygame.display.set_caption("Pierwsza gra w Pygame")

player = pygame.rect.Rect(config.x, config.y, config.width, config.height)  # tworzy kwadrat reprezentujący gracza

clock = pygame.time.Clock()
walk_cooldown = 0
# opóźnienie między ruchami
walk_delay = 1
# domyślny obrót gracza po uruchomieniu gry
last_move = "down"

run = True
while run:
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknął okno gry
            run = False

    keys = pygame.key.get_pressed()
    # zmniejszenie licznika czasu do następnego ruchu
    delta = clock.tick() / 150.0
    walk_cooldown -= delta

    if walk_cooldown <= 0:
        if keys[pygame.K_RIGHT]:  # jeśli naciśnięta jest strzałka w prawo
            config.x += config.speed
            walk_cooldown = walk_delay  # ustawia z powrotem licznik czasu do następnego ruchu
            last_move = "right"
            sound.play_sound("player_move")
        if keys[pygame.K_LEFT]:  # strzałka w lewo
            config.x -= config.speed
            walk_cooldown = walk_delay
            last_move = "left"
            sound.play_sound("player_move")
        if keys[pygame.K_UP]:  # strzałka w górę
            config.y -= config.speed
            walk_cooldown = walk_delay
            last_move = "up"
            sound.play_sound("player_move")
        if keys[pygame.K_DOWN]:  # strzałka w dół
            config.y += config.speed
            walk_cooldown = walk_delay
            last_move = "down"
            sound.play_sound("player_move")

        player = pygame.rect.Rect(config.x, config.y, config.width, config.height)  # odświeżenie pozycji gracza

    window.fill((0, 0, 0))

    window.blit(movement.get_player_sprite(last_move), player)
    pygame.display.update()

pygame.quit()
