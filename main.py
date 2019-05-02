#! /usr/bin/env python3
# coding: utf-8
import os
import pygame
import time
from macgyver_game.events.events import quitting
from macgyver_game.game.game import Game


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    keep_playing = True  # It will be true until the player win or die
    size = 680
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    pygame.key.set_repeat(10, 10)
    screen = pygame.display.set_mode((size, size), pygame.DOUBLEBUF)
    game = Game(dir_path)
    previous_time = time.time()
    pygame.mixer.music.play()

    while keep_playing:
        actual_time = time.time()
        if actual_time - previous_time >= 0.08:
            # make all the action needed
            game.action(screen)
            keep_playing = quitting(game.macgyver, game.guard)
            previous_time = time.time()

    game.ending_game(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
