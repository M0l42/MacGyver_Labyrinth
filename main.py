import pygame


class Map:
    def __init__(self):
        self.case = [[0] * 15 for i in range(15)]
        self.surface = pygame.image.load("pictures/labyrinthe.png").convert()


class Character:
    def __init__(self, x, y, picture):
        self.x = x
        self.y = y
        self.alive = True
        self.surface = pygame.image.load("pictures/" + picture).convert()


class MacGyver(Character):
    def move(self):
        pass


class Items:
    pass


def main():
    keep_playing = True
    pygame.init()

    pygame.key.set_repeat(10, 10)

    screen = pygame.display.set_mode((340,340), pygame.DOUBLEBUF)

    map = Map()
    macGyver = MacGyver(0, 0, "MacGyver.png")
    guard = Character(14, 14, "Gardien.png")

    while keep_playing:
        screen.blit(map.surface, (0, 0))
        pygame.display.flip()
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False

    pygame.quit()


main()
