import pygame
import sys
import random


def mov_pipes(pipes):
    for pipe in pipes:
         pipe.centerx -= 2
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom > 400:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False,True)
            screen.blit(flip_pipe,pipe)


pygame.init()
screen = pygame.display.set_mode((218, 512))
clock = pygame.time.Clock()

# game variables
gravity = 0.07

bird_movement = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
# floor_surface =

floor_x_pos = 0

# import image of bird
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center=(50, 218))
# pipe surface
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [150,200,175,125,145]


# pipes


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 430))
    screen.blit(floor_surface, (floor_x_pos + 218, 430))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(200, (random_pipe_pos)))
    top_pipe = pipe_surface.get_rect(midbottom=(200, (random_pipe_pos - 100)))
    return bottom_pipe, top_pipe


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0

                bird_movement -= 4
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
    screen.blit(bg_surface, (0, 0))

    # bird movement
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1

    # pipes
    pipe_list = mov_pipes(pipe_list)
    draw_pipes(pipe_list)

    draw_floor()
    if floor_x_pos <= -218:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
