import pygame
from hyperparameters import *

def kolizija(walls, pacman):
    da = False;
    for wall in walls:
        if(pygame.Rect.colliderect(wall, pacman.pos_x-pacman.radius, pacman.pos_y-pacman.radius, pacman.radius*2, pacman.radius*2)):
            da = True
    return da
            

def make_wall(start_x, start_y, width, hight):
    wall = pygame.Rect(((start_x)*SCALE_FACTOR), ((start_y)*SCALE_FACTOR), width*SCALE_FACTOR, hight*SCALE_FACTOR)
    return wall

walls = []

#BLOCKS_X = 23
#BLOCKS_Y = 20

walls.append(make_wall(0, 0, 1, 21)) #M
walls.append(make_wall(0, 0, 23, 1)) #N
walls.append(make_wall(0, 20, 23, 1)) #P
walls.append(make_wall(22, 0, 1, 21)) #O
walls.append(make_wall(3, 1, 3, 4)) #A
walls.append(make_wall(17, 1, 3, 4)) #B
walls.append(make_wall(3, 7, 2, 7)) #E
walls.append(make_wall(3, 16, 3, 4)) #C
walls.append(make_wall(8, 1, 7, 1)) #S
walls.append(make_wall(8, 4, 7, 1)) #L
walls.append(make_wall(18, 7, 2, 7)) #F
walls.append(make_wall(17, 16, 3, 4)) #D
walls.append(make_wall(8, 16, 1, 4)) #G
walls.append(make_wall(9, 18, 5, 2)) #Q
walls.append(make_wall(14, 16, 1, 4)) #R
walls.append(make_wall(7, 7, 1, 7)) #H
walls.append(make_wall(7, 13, 8, 1)) #I
walls.append(make_wall(15, 7, 1, 7)) #J
walls.append(make_wall(10, 7, 3, 4)) #K
walls.append(make_wall(11, 14, 1, 2)) #T


#walls.append(make_wall())