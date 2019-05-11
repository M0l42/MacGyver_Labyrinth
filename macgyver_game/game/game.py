import os
import pygame
from time import time
from macgyver_game.models.character import Character, MacGyver
from macgyver_game.models.items import Items


class Game:

    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.length = 15
        self.case_length = 40

        # Initialize the background and labyrinthe's image
        self.background_image = pygame.image.load(
            os.path.join(self.dir_path, "pictures", "screen.png")).convert()
        self.labyrinth_shown = pygame.image.load(
            os.path.join(self.dir_path, "pictures", "labyrinth_alpha.png")).convert_alpha()
        self.labyrinth = pygame.image.load(
            os.path.join(self.dir_path, "pictures", "labyrinth.png")).convert()

        # Load the music
        pygame.mixer.music.load(os.path.join(self.dir_path, "sounds", "MacGyver_generique.mp3"))
        pygame.mixer.music.set_volume(0.2)

        # Initialize our character
        self.macgyver = MacGyver(1, 1, self.dir_path, "MacGyver.png")
        self.guard = Character(self.length, self.length, self.dir_path, "Guard.png")

        # Initialize our Items
        self.items = []
        # Load the Images and sounds
        self.items.append(Items(self.dir_path, "needle2.png"))
        self.items.append(Items(self.dir_path, "ether.png"))
        self.items.append(Items(self.dir_path, "plastic_tube.png"))
        self.items_sounds = pygame.mixer.Sound(os.path.join(self.dir_path, "sounds", "get_item.wav"))

        for i in range(0, 3):
            self.items[i].get_random_position(i, self.items)

    def display(self, screen):
        # This is where we'll blit all our image to the screen
        centering = 3
        # A small variable to shift our image to make them more center in their case
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.labyrinth_shown, (0, 0))
        if self.macgyver.alive is True:
            screen.blit(self.macgyver.surface, (self.macgyver.y * self.case_length + centering,
                                                self.macgyver.x * self.case_length + centering))
        if self.guard.alive is True:
            screen.blit(self.guard.surface, (self.guard.y * self.case_length + centering,
                                             self.guard.x * self.case_length + centering))
        for i in self.items:
            if i.picked is False:
                # We only show the items which are not picked yet
                screen.blit(i.surface, (i.y * self.case_length + centering,
                                        i.x * self.case_length + centering))
        pygame.display.flip()

    def picking_item(self):
        # Checking with every item if MacGyver step on it
        for i in self.items:
            if (self.macgyver.x, self.macgyver.y) == (i.x, i.y) and i.picked is False:
                i.picked = True
                # To make us know the item is picked, so we don't show them or picked them again
                self.macgyver.items_picked += 1
                self.items_sounds.play()

    def action(self, screen):
        # We regroup all action the game will need in one method.
        self.display(screen)
        self.macgyver.move(pygame.key.get_pressed(), self.labyrinth, self.case_length)
        self.picking_item()

    def ending_game(self, screen):
        # We need to stop the music to play another one
        pygame.mixer.music.stop()
        actual_time = time()
        previous_time = time()
        time_song_is_playing = 0
        if self.macgyver.win is True:
            # Showing the winning screen with music
            end_game_screen = pygame.image.load(os.path.join(self.dir_path, "pictures", "winning.jpg")).convert()
            pygame.mixer.music.load(os.path.join(self.dir_path, "sounds", "winning.mp3"))
            time_song_is_playing = 6
        elif self.macgyver.win is False:
            # Showing the loosing screen with music
            end_game_screen = pygame.image.load(os.path.join(self.dir_path, "pictures", "loosing.jpg")).convert()
            pygame.mixer.music.load(os.path.join(self.dir_path, "sounds", "game_over.mp3"))
            time_song_is_playing = 8

        pygame.mixer.music.play()
        while actual_time - previous_time < time_song_is_playing:
            # Display the screen as long as the song is playing
            actual_time = time()
            screen.blit(end_game_screen, (0, 0))
            pygame.display.flip()
