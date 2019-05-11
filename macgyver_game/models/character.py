import pygame
import os

white = (255, 255, 255)


class Character:
    # Initialization of the character
    def __init__(self, x, y, dir_path, picture_name):
        self.x = x
        self.y = y
        self.alive = True
        self.surface = pygame.image.load(os.path.join(dir_path, "pictures/", picture_name)).convert_alpha()


class MacGyver(Character):
    # How MacGyver will move depending on the keys pressed
    items_picked = 0
    win = None

    def move(self, keystate, labyrinth, case_length):
        if keystate[pygame.K_UP]:
            if labyrinth.get_at((self.y * case_length + 15, self.x * case_length)) == white and self.x > 0:
                self.x -= 1
        if keystate[pygame.K_DOWN]:
            if labyrinth.get_at(
                    (self.y * case_length + 15, self.x * case_length + case_length)) == white and self.x < 15:
                self.x += 1
        if keystate[pygame.K_RIGHT]:
            if labyrinth.get_at(
                    (self.y * case_length + case_length, self.x * case_length + 15)) == white and self.y < 15:
                self.y += 1
        if keystate[pygame.K_LEFT]:
            if self.y != 1:
                if labyrinth.get_at((self.y * case_length, self.x * case_length + 15)) == white and self.y > 0:
                    self.y -= 1
