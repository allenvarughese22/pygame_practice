import pygame
import random
import math
from pygame import  mixer

# initialize the pygame

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# title and icon
pygame.display.set_caption('spaceinvader')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# playerimage
playerIMG = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerXchange = 0

# alienimage
enemyrIMG = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
numb_enemies = 3

for i in range(numb_enemies):
    enemyrIMG.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    print(enemyX)
    print(enemyY)
    enemyXchange.append(3)
    enemyYchange.append(10)

# bulleimage
bulletIMG = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
# bulletXchange = 3
bulletYchange = 10
bullet_state = 'ready'

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# collision function

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 25:
        return True
    else:
        return False


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIMG, (x + 16, y + 10))


def player(x, y):

    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyrIMG[i], (x, y))

def show_score(x,y):

    score_method = font.render('Score:' + str(score), True, (255, 0, 255))
    screen.blit(score_method, (x,y))
# game loop
running = True

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -6
            if event.key == pygame.K_RIGHT:
                playerXchange = 6
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound =mixer.Sound('laser.wav')
                    bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX += playerXchange

    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    for i in range(numb_enemies):

        enemyX[i] += enemyXchange[i]

        if enemyX[i] <= 0:
            enemyXchange[i] = 3
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] > 736:
            enemyXchange[i] = - 3

            enemyY[i] += enemyYchange[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 100)


    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    player(playerX, playerY)
    for i in range(numb_enemies):
        enemy(enemyX[i], enemyY[i], i)


    show_score(textX,textY)
    pygame.display.update()
