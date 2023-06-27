from hyperparameters import *
import pygame
from collision import *
from walls import *

#direction 1-levo, 2-desno, 3-dole, 4-gore

class Pacman:
    def __init__(self, pos_x, pos_y, radius, color, speed, start_direction, sprite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius*SCALE_FACTOR/2
        self.color = color
        self.speed = speed
        self.direction = start_direction
        self.prev_direction = start_direction
        self.sprite = sprite
        self.sprite = pygame.transform.scale(sprite, (self.radius*2, self.radius*2))
    def update(self, keys):
        if(keys[pygame.K_a]):
            self.direction = 1
        if(keys[pygame.K_d]):
            self.direction = 2
        if(keys[pygame.K_s]):
            self.direction = 3
        if(keys[pygame.K_w]):
            self.direction = 4

        if(self.direction == 1):
            self.pos_x -= 1*self.speed
            if(kolizija(walls, self) and self.prev_direction != self.direction):
                self.direction = self.prev_direction
            self.pos_x += 1*self.speed
        if(self.direction == 2):
            self.pos_x += 1*self.speed
            if(kolizija(walls, self) and self.prev_direction != self.direction):
                self.direction = self.prev_direction
            self.pos_x -= 1*self.speed
        if(self.direction == 3):
            self.pos_y += 1*self.speed
            if(kolizija(walls, self) and self.prev_direction != self.direction):
                self.direction = self.prev_direction
            self.pos_y -= 1*self.speed
        if(self.direction == 4):
            self.pos_y -= 1*self.speed
            if(kolizija(walls, self) and self.prev_direction != self.direction):
                self.direction = self.prev_direction
            self.pos_y += 1*self.speed

        if(self.direction == 1):
            self.pos_x -= 1*self.speed
            if(kolizija(walls, self)):
                self.pos_x += 1*self.speed
        if(self.direction == 2):
            self.pos_x += 1*self.speed
            if(kolizija(walls, self)):
                self.pos_x -= 1*self.speed
        if(self.direction == 3):
            self.pos_y += 1*self.speed
            if(kolizija(walls, self)):
                self.pos_y -= 1*self.speed
        if(self.direction == 4):
            self.pos_y -= 1*self.speed
            if(kolizija(walls, self)):
                self.pos_y += 1*self.speed
        self.prev_direction = self.direction

    def draw(self, screen):
        screen.blit(self.sprite, (self.pos_x-self.radius, self.pos_y-self.radius))
        #pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)
    