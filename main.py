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
    # Pre init the mixer help pygame with the buffer of pygame.mixer
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    # pygame.key.set_repeat(10, 10)
    screen = pygame.display.set_mode((size, size), pygame.DOUBLEBUF)

    # code to generate a background image
    # background = pygame.image.load(os.path.join(dir_path, "pictures/background.png")).convert()
    # for i in range(size/40):
    #    for j in range(size/40):
    #        screen.blit(background, (i*40, j*40))
    # pygame.image.save(screen, dir_path, "picture/screen.png")

    game = Game(dir_path)
    previous_time = time.time()
    pygame.mixer.music.play()

    while keep_playing:
        actual_time = time.time()
        if actual_time - previous_time >= 0.1:
            # make all the action needed
            game.action(screen)
            keep_playing = quitting(game.macgyver, game.guard, pygame.key.get_pressed())
            previous_time = actual_time

    game.ending_game(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
