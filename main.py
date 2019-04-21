#! /usr/bin/env python3
# coding: utf-8

import pygame
import time
from macgyver_game.models.character import Character, MacGyver
from macgyver_game.models.items import Items
from macgyver_game.events.events import keyboard, quitting


def main():
    keep_playing = True  # It will be true until the player win or die
    case_length = 40

    pygame.init()

    pygame.key.set_repeat(10, 10)

    screen = pygame.display.set_mode((680, 680), pygame.DOUBLEBUF)

    labyrinth = pygame.image.load("pictures/labyrinthe.png").convert()
    macgyver = MacGyver(1, 1, "MacGyver.png")
    guard = Character(15, 15, "Gardien.png")

    items = []
    items.append(Items("aiguille.png"))
    items.append(Items("ether.png"))
    items.append(Items("tube_plastique.png"))
    for i in range(0, 3):
        items[i].get_random_position(i, items)

    previous_time = time.time()

    while keep_playing:
        actual_time = time.time()
        if actual_time - previous_time >= 0.08:
            # bliting the all the image to the screen
            screen.blit(labyrinth, (0, 0))
            if macgyver.alive is True:
                screen.blit(macgyver.surface, (macgyver.y*case_length+3, macgyver.x*case_length+3))
            if guard.alive is True:
                screen.blit(guard.surface, (guard.y * case_length + 3, guard.x * case_length + 3))
            for i in items:
                if i.picked is False:
                    screen.blit(i.surface, (i.y * case_length + 3, i.x * case_length + 3))
            # Displaying the new screen
            pygame.display.flip()
            # Getting the value of the key pressed by the player
            macgyver.move(keyboard(), labyrinth, case_length)
            for i in items:
                if (macgyver.x, macgyver.y) == (i.x, i.y) and i.picked is False:
                    i.picked = True
                    macgyver.items_picked += 1
            keep_playing = quitting(macgyver, guard)
            previous_time = time.time()

    pygame.quit()


if __name__ == "__main__":
    main()
