import pygame


def quitting(macgyver, guard):
    keep_playing = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_playing = False
        else:
            keep_playing = True
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
    return keep_playing

def keyboard():
    return pygame.key.get_pressed()
