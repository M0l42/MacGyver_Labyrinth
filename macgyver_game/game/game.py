import pygame
from macgyver_game.models.character import Character, MacGyver
from macgyver_game.models.items import Items
from macgyver_game.events.events import keyboard


class Game:

    def __init__(self):
        self.length = 15
        self.case_length = 40

        self.labyrinth = pygame.image.load("pictures/labyrinthe.png").convert()
        pygame.mixer.music.load("sounds/MacGyver_generique.mp3")

        self.macgyver = MacGyver(1, 1, "MacGyver.png")
        self.guard = Character(self.length, self.length, "Gardien.png")

        self.items = []
        self.items.append(Items("aiguille.png"))
        self.items.append(Items("ether.png"))
        self.items.append(Items("tube_plastique.png"))
        self.items_sounds = pygame.mixer.Sound("sounds/get_item.wav")
        for i in range(0, 3):
            self.items[i].get_random_position(i, self.items)

    def display(self, screen):
        screen.blit(self.labyrinth, (0, 0))
        if self.macgyver.alive is True:
            screen.blit(self.macgyver.surface, (self.macgyver.y * self.case_length + 3, self.macgyver.x * self.case_length + 3))
        if self.guard.alive is True:
            screen.blit(self.guard.surface, (self.guard.y * self.case_length + 3, self.guard.x * self.case_length + 3))
        for i in self.items:
            if i.picked is False:
                screen.blit(i.surface, (i.y * self.case_length + 3, i.x * self.case_length + 3))
        pygame.display.flip()

    def picking_item(self):
        for i in self.items:
            if (self.macgyver.x, self.macgyver.y) == (i.x, i.y) and i.picked is False:
                i.picked = True
                self.macgyver.items_picked += 1
                self.items_sounds.play()

    def action(self, screen):
        self.display(screen)
        self.macgyver.move(keyboard(), self.labyrinth, self.case_length)
        self.picking_item()
