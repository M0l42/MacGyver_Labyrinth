#! /usr/bin/env python3
# coding: utf-8

import pygame
import time
from random import *

white = (255,255,255)


class Map:
    # Loading the map
    def __init__(self):
        self.surface = pygame.image.load("pictures/labyrinthe.png").convert()


class Character:
    # Initialization of the character
    def __init__(self, x, y, picture_name):
        self.x = x
        self.y = y
        self.alive = True
        self.surface = pygame.image.load("pictures/" + picture_name).convert_alpha()


class MacGyver(Character):
    # How MacGyver will move depending on the keys pressed
    def move(self, keystate, labyrinth, case_length):
        if keystate[pygame.K_UP]:
            if labyrinth.surface.get_at((self.y*case_length+15, self.x*case_length)) == white:
                self.x -= 1
        if keystate[pygame.K_DOWN]:
            if labyrinth.surface.get_at((self.y*case_length+15, self.x*case_length + case_length)) == white:
                self.x += 1
        if keystate[pygame.K_RIGHT]:
            if labyrinth.surface.get_at((self.y*case_length + case_length, self.x*case_length+15)) == white:
                self.y += 1
        if keystate[pygame.K_LEFT]:
            if labyrinth.surface.get_at((self.y*case_length, self.x*case_length+15)) == white:
                self.y -= 1


class Items:
    def __init__(self, picture_name):
        self.picked = False
        self.surface = pygame.image.load("pictures/" + picture_name).convert_alpha()
        self.x = None
        self.y = None

    def get_random_position(self, i, items):
        position_not_taken = False
        while position_not_taken is False:
            self.x = randint(1, 15)
            self.y = randint(1, 15)
            if (self.x, self.y) != (0, 0) or (self.x, self.y) != (15, 15):
                if i == 0:
                    position_not_taken = True
                else:
                    for j in range(0, i):
                        if (self.x, self.y) != (items[j].x, items[j].y):
                            position_not_taken = True
                        else:
                            position_not_taken = False


def main():
    keep_playing = True  # It will be true until the player win or die
    case_length = 40
    items_picked = 0

    pygame.init()

    pygame.key.set_repeat(10, 10)

    screen = pygame.display.set_mode((680, 680), pygame.DOUBLEBUF)

    labyrinth = Map()
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
        if actual_time - previous_time >= 0.08:
            # bliting the all the image to the screen
            screen.blit(labyrinth.surface, (0, 0))
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
            keystate = pygame.key.get_pressed()
            macgyver.move(keystate, labyrinth, case_length)
            for i in items:
                if (macgyver.x, macgyver.y) == (i.x, i.y) and i.picked is False:
                    i.picked = True
                    items_picked += 1
            if (macgyver.x, macgyver.y) == (guard.x, guard.y):
                if items_picked == 3:
                    guard.alive = False
                else:
                    macgyver.alive = False
                    keep_playing = False
            if macgyver.x == 16:
                keep_playing = False
            previous_time = time.time()

    pygame.quit()

if __name__ == "__main__":
    main()
