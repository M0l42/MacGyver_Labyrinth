import pygame


def quitting(macgyver, guard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        else:
            return True
    if (macgyver.x, macgyver.y) == (guard.x, guard.y):
        if macgyver.items_picked == 3:
            guard.alive = False
            return True
        else:
            macgyver.alive = False
            return False
    if macgyver.y == 16:
        return False
    else:
        return True


def keyboard():
    return pygame.key.get_pressed()
