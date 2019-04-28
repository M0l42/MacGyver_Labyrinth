#! /usr/bin/env python3
# coding: utf-8

import pygame
import time
from macgyver_game.events.events import quitting
from macgyver_game.game.game import Game


def main():
    keep_playing = True  # It will be true until the player win or die
    size = 680
    pygame.init()
    pygame.mixer.init()
    pygame.key.set_repeat(10, 10)
    screen = pygame.display.set_mode((size, size), pygame.DOUBLEBUF)
    game = Game()
    previous_time = time.time()
    pygame.mixer.music.play()
    music_playing = True

    while keep_playing:
        actual_time = time.time()
        if actual_time - previous_time >= 0.08:
            # make all the action needed
            game.action(screen)
            keep_playing = quitting(game.macgyver, game.guard)
            previous_time = time.time()

    game.ending_game()

    pygame.mixer.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
