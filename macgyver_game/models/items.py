import pygame
import os
from random import randint


class Items:
    """
    This class will handle the items
    It will mostly put an random position for every item
    and initialise it with image and has an variable
    to tell if it's picked or not
    """
    def __init__(self, dir_path, picture_name):
        self.picked = False
        self.surface = pygame.image.load(os.path.join(dir_path, "pictures/", picture_name)).convert_alpha()
        self.x = None
        self.y = None

    def get_random_position(self, i, items, macgyver, guard ):
        # Look if there's already something in the position given until the case chosen is free
        position_not_taken = False
        while position_not_taken is False:
            self.x = randint(1, 15)
            self.y = randint(1, 15)
            if (self.x, self.y) != (macgyver.x, macgyver.y) and (self.x, self.y) != (guard.x, guard.y):
                if i == 0:
                    position_not_taken = True
                else:
                    for j in range(0, i):
                        if (self.x, self.y) != (items[j].x, items[j].y):
                            position_not_taken = True
                        else:
                            position_not_taken = False
                            j = i
