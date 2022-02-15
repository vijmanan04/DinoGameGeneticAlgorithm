import pygame
import random





def metrics(num, obstacles, d1, SCREEN, game_speed):

    obstacleDistance = 0
    obstacleHeightBottom = 0
    obstacleHeightTop = 0
    obstacleWidth = 0

    dinoHeightBottom = 0
    dinoHeightTop = 0
    dinoWidth = 0

    game_speed = game_speed

    if len(obstacles) > 0:
        obstacle = obstacles[num]
    else:
        return 1

    font = pygame.font.Font('freesansbold.ttf', 15)

    obstacleDistance = obstacle.rect.x - (d1.dino_rect.x + d1.dino_rect.width)
    obstacleHeightTop = obstacle.rect.y
    obstacleHeightBottom = obstacle.rect.y - obstacle.rect.height
    obstacleWidth = obstacle.rect.width

    dinoHeightTop = d1.dino_rect.y
    dinoHeightBottom = d1.dino_rect.y - d1.dino_rect.height
    dinoWidth = d1.dino_rect.width

    text1 = font.render(f"Dino Height Top: {dinoHeightTop}",True, (0,0,0))
    text1Rect = text1.get_rect()
    text1Rect.midleft = (20, 10)

    text2 = font.render(f"Dino Height Bottom: {dinoHeightBottom}", True, (0,0,0))
    text2Rect = text2.get_rect()
    text2Rect.midleft = (20, 40)

    text3 = font.render(f"Next Obstacle Distance: {obstacleDistance}", True, (0,0,0))
    text3Rect = text3.get_rect()
    text3Rect.midleft = (20, 70)

    text4 = font.render(f"Next Obstacle Height Top: {obstacleHeightTop}", True, (0,0,0))
    text4Rect = text4.get_rect()
    text4Rect.midleft = (20, 100)

    text5 = font.render(f"Next Obstacle Height Bottom: {obstacleHeightBottom}", True, (0,0,0))
    text5Rect = text5.get_rect()
    text5Rect.midleft = (20, 130)

    text6 = font.render(f"Obstacle Width: {obstacleWidth}", True, (0,0,0))
    text6Rect = text6.get_rect()
    text6Rect.midleft = (20, 160)

    text7 = font.render(f"Dino Width: {dinoWidth}", True, (0,0,0))
    text7Rect = text7.get_rect()
    text7Rect.midleft = (20, 190)

    SCREEN.blit(text1, text1Rect)
    SCREEN.blit(text2, text2Rect)
    SCREEN.blit(text3, text3Rect)
    SCREEN.blit(text4, text4Rect)
    SCREEN.blit(text5, text5Rect)
    SCREEN.blit(text6, text6Rect)
    SCREEN.blit(text7, text7Rect)

    return [obstacleDistance, obstacleHeightBottom, obstacleHeightTop, obstacleWidth, dinoHeightBottom, dinoHeightTop, dinoWidth, game_speed]

def score(points, game_speed, SCREEN):
    points += 0.5
    if (points % 100 == 0):
        game_speed += 1
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Score: " + str(points), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (900, 40)
    SCREEN.blit(text, textRect)
    return points, game_speed

def obstacleAppend(obstacles, Obstacle, SCREEN_WIDTH):
    if len(obstacles) == 0:
        if random.randint(0, 2) == 0:
            obstacles.append(Obstacle.SmallCactus(SCREEN_WIDTH))
            return -1

        elif random.randint(0, 2) == 1:
            obstacles.append(Obstacle.LargeCactus(SCREEN_WIDTH))
            return 0

        elif random.randint(0, 2) == 2:
            obstacles.append(Obstacle.Bird(SCREEN_WIDTH))
            return 1

def obstacleCollide(obstacles, game_speed, SCREEN, d1):
    for obstacle in obstacles:
        obstacle.draw(SCREEN)
        obstacle.update(game_speed, obstacles)

        if d1.dino_rect.colliderect(obstacle.rect):
            pygame.draw.rect(SCREEN, (255,0,0), d1.dino_rect, 2)
