import pygame


class Map:
    def __init__(self):
        pass

    def generate_map(self):
        pass


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        pass


class MacGyver(Character):
    def move(self):
        pass


class Items:
    pass


def main():
    pygame.init()

    pygame.key.set_repeat(10,10)

    pygame.quit()


main()
