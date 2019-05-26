import pygame
import os


class Character:
    """
    this class is the one for the character
    it will get the position found in map's file
    and load the image of the character
    """
    def __init__(self, length, case_length, color, dir_path, picture_name, labyrinth):
        self.x = 0
        self.y = 0
        self.get_initial_position(labyrinth, length, case_length, color)
        self.alive = True
        self.surface = pygame.image.load(os.path.join(dir_path, "pictures/", picture_name)).convert_alpha()

    def get_initial_position(self, labyrinth, length, case_length, color):
        for i in range(length):
            for j in range(length):
                if labyrinth.get_at((i * case_length + int(case_length/2),
                                     j * case_length + int(case_length/2))) == color:
                    self.x = i
                    self.y = j


class MacGyver(Character):
    """
    This class inherited from the Character class
    It will add the method to handle the movement system
    """
    items_picked = 0
    win = None

    def move(self, keystate, labyrinth, case_length, white):
        # How MacGyver will move depending on the keys pressed
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
