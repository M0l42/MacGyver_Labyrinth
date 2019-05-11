import pygame


def quitting(macgyver, guard, keystate):
    keep_playing = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keystate[pygame.K_ESCAPE]:
            keep_playing = False

    if (macgyver.x, macgyver.y) == (guard.x, guard.y):
        if macgyver.items_picked == 3:
            guard.alive = False
            macgyver.win = True
            print("You win !")
            keep_playing = False
        else:
            macgyver.alive = False
            print("You loose !")
            keep_playing = False
            macgyver.win = False
    return keep_playing
