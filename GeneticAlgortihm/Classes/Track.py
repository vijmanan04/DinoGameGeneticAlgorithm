import pygame
import os

TRACK = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]

class Track:
    X_POS = 0
    def __init__(self):
        self.image = TRACK[0]
        self.image_rect = self.image.get_rect()
        self.width = self.image_rect.width
        self.image_rect.x = self.X_POS
        self.image_rect.y = 370

    def draw(self, SCREEN, game_speed):
        self.image_rect.x -= game_speed

        SCREEN.blit(self.image, (self.image_rect.x, self.image_rect.y))
        SCREEN.blit(self.image, (self.image_rect.x + self.width, self.image_rect.y))

        if (self.image_rect.x <= -self.width):
            SCREEN.blit(self.image, (self.image_rect.x + self.width, self.image_rect.y))
            self.image_rect.x = 0
