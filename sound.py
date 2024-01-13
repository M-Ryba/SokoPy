import pygame
import assets
pygame.init()


def play_sound(sound_name):
    if sound_name in assets.sounds:
        assets.sounds[sound_name].play()
        return 1
    else:
        assets.sounds["error"].play()
        return -1
