
# import pygame module in this program
import pygame
import os
import random
from Classes import Dinosaur
from Classes import Cloud
from Classes import Obstacle
from Classes import Track
from Assets import HelperFunctions as HF

# activate pygame module
pygame.init()

# Global Variables
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 500
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))


# set the pygame window name
pygame.display.set_caption('Dinosaur Game')


# Define Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)


#GAME_OVER = [pygame.image.load(os.path.join("Assets/Other", "GameOver.png"))]
#RESET = [pygame.image.load(os.path.join("Assets/Other", "Reset.png"))]

# main dino_game environment
def main():
    game_speed = 14
    points = 0

    # Load classes
    d1 = Dinosaur.Dinosaur()
    c1 = Cloud.Cloud(SCREEN_WIDTH)
    t1 = Track.Track()

    # Initialize pygame clock for FPS setting
    clock = pygame.time.Clock()

    obstacles = []

    while True :

        SCREEN.fill(WHITE)
        userInput = pygame.key.get_pressed()

        d1.draw(SCREEN)
        c1.draw(SCREEN)
        t1.draw(SCREEN, game_speed)


        type = HF.obstacleAppend(obstacles, Obstacle, SCREEN_WIDTH)
        HF.obstacleCollide(obstacles, game_speed, SCREEN, d1)
        points, game_speed = HF.score(points, game_speed, SCREEN)
        metrics = HF.metrics(0, obstacles, d1, SCREEN, game_speed)

        d1.update(userInput, game_speed)
        c1.update(game_speed)


        d1.think(metrics)




        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(30) # 30 FPS
main()
