import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((218, 512))
clock = pygame.time.Clock()

# game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
# floor_surface =

floor_x_pos = 0

# import image of bird
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center=(50, 218))


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 430))
    screen.blit(floor_surface, (floor_x_pos + 218, 430))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0

                bird_movement -= 8

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1

    draw_floor()
    if floor_x_pos <= -218:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
