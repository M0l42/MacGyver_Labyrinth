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
        self.surface = pygame.image.load("pictures/" + picture).convert_alpha()


class MacGyver(Character):
    def move(self):
        pass


class Items:
    pass


def main():
    keep_playing = True
    case_length = 40
    pygame.init()

    pygame.key.set_repeat(10, 10)

    screen = pygame.display.set_mode((680, 680), pygame.DOUBLEBUF)

    labyrinth = Map()
    macgyver = MacGyver(1, 1, "MacGyver.png")
    guard = Character(15, 15, "Gardien.png")

    while keep_playing:
        screen.blit(labyrinth.surface, (0, 0))
        screen.blit(macgyver.surface, (macgyver.y*case_length+3, macgyver.x*case_length+3))
        screen.blit(guard.surface, (guard.y * case_length + 3, guard.x * case_length + 3))
        pygame.display.flip()
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False

    pygame.quit()


main()
