import pygame
import time

white = (255,255,255)


class Map:
    # Loading the map
    def __init__(self):
        self.surface = pygame.image.load("pictures/labyrinthe.png").convert()


class Character:
    # Initialization of the character
    def __init__(self, x, y, picture):
        self.x = x
        self.y = y
        self.alive = True
        self.surface = pygame.image.load("pictures/" + picture).convert_alpha()


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
    pass


def main():
    keep_playing = True  # It will be true until the player win or die
    case_length = 40

    pygame.init()

    pygame.key.set_repeat(10, 10)

    screen = pygame.display.set_mode((680, 680), pygame.DOUBLEBUF)

    labyrinth = Map()
    macgyver = MacGyver(1, 1, "MacGyver.png")
    guard = Character(15, 15, "Gardien.png")
    previous_time = time.time()

    while keep_playing:
        actual_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
        if actual_time - previous_time >= 0.08:
            # bliting the all the image to the screen
            screen.blit(labyrinth.surface, (0, 0))
            screen.blit(macgyver.surface, (macgyver.y*case_length+3, macgyver.x*case_length+3))
            screen.blit(guard.surface, (guard.y * case_length + 3, guard.x * case_length + 3))
            # Displaying the new screen
            pygame.display.flip()
            # Getting the value of the key pressed by the player
            keystate = pygame.key.get_pressed()
            macgyver.move(keystate, labyrinth, case_length)
            previous_time = time.time()

    pygame.quit()


main()
