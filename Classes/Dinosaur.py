import pygame
import os
import sys

from Classes import NN
import numpy as np

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")), pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]


class Dinosaur:
    X_POS = 50
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 7.5
    brain = NN.NeuralNetwork(8, 4, 1, np.random.randn(8, 4), np.random.randn(4, 1), 1, 1)

    def __init__(self):
        self.duck_img = DUCKING
        self.jump_img = JUMPING
        self.run_img = RUNNING

        self.dino_duck = False
        self.dino_jump = False
        self.dino_run = True

        self.jump_vel = self.JUMP_VEL

        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect(width = 60, height = 60)
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0


    def think(self, metrics):
        self.prediction = self.brain.predict(metrics)
    



    def update(self, userInput, game_speed):
        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump and (self.dino_rect.y == self.Y_POS):
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump(game_speed)


    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect(width = 60, height = 60)
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect(width = 60, height = 60)
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self, game_speed):
        self.image = self.jump_img[0]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * (5)
            self.jump_vel -= 0.7 + game_speed*0.01
        if self.jump_vel <= - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
