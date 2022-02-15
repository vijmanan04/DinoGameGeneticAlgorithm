import pygame
import os
import random

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

class Obstacle:
    global obstacles
    def __init__(self, image, type, SCREEN_WIDTH):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH + 400

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], (self.rect.x, self.rect.y))


class SmallCactus(Obstacle):
    def __init__(self, SCREEN_WIDTH):
        self.type = random.randint(0, 2)
        super().__init__(SMALL_CACTUS, self.type, SCREEN_WIDTH)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, SCREEN_WIDTH):
        self.type = random.randint(0, 2)
        super().__init__(LARGE_CACTUS, self.type, SCREEN_WIDTH)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, SCREEN_WIDTH):
        self.type = 0
        super().__init__(BIRD, self.type, SCREEN_WIDTH)
        self.height = [250, 300]
        self.rect.y = self.height[random.randint(0,1)]
        self.index = 0


    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
