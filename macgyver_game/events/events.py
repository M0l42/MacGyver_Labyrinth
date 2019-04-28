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
            print("You loose !")
            return False
    if macgyver.y == 16:
        macgyver.win = True
        print("You win !")
        return False
    else:
        return True


def keyboard():
    return pygame.key.get_pressed()
