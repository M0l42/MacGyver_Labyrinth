#! /usr/bin/env python3
# coding: utf-8

import pygame
import time
from macgyver_game.events.events import keyboard, quitting
from macgyver_game.game.game import Game


def main():
    keep_playing = True  # It will be true until the player win or die
    pygame.init()
    pygame.key.set_repeat(10, 10)
    screen = pygame.display.set_mode((680, 680), pygame.DOUBLEBUF)
    game = Game()
    previous_time = time.time()

    while keep_playing:
        actual_time = time.time()
        if actual_time - previous_time >= 0.08:
            # bliting the all the image to the screen
            game.display(screen)
            # Displaying the new screen
            pygame.display.flip()
            # Getting the value of the key pressed by the player
            game.macgyver.move(keyboard(), game.labyrinth, game.case_length)
            game.picking_item()
            keep_playing = quitting(game.macgyver, game.guard)
            previous_time = time.time()

    pygame.quit()


if __name__ == "__main__":
    main()
