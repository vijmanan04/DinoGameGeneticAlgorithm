import pygame
import os
import random

CLOUD = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

class Cloud:
    def __init__(self, SCREEN_WIDTH):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.image = CLOUD[0]
        self.width = self.image.get_width()
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)


    def update(self, game_speed):
        self.x -= game_speed
        if (self.x < - self.width):
            self.x = self.SCREEN_WIDTH + random.randint(800,1000)
            self.y = random.randint(50,100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
