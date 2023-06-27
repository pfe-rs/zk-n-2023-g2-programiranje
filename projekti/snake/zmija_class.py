import pygame
from collison import collision
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

class Zmija:
    kx = 0
    ky = 0
    zmija_list = []
    size = 1
    x = 0
    y = 0
    def __init__(self, _x, _y, _speed, _width, _height):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.color = ('#20df54')
        self.width = _width
        self.height = _height
        self.zmija_list.append((self.x,self.y))
    
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)
    def draw_i(self, screen, i):
         rect1 = pygame.Rect(self.zmija_list[i][0], self.zmija_list[i][1], self.width, self.height)
         pygame.draw.rect(screen, self.color, rect1)
         
    def update(self, keys, dt):

        if keys[pygame.K_a] and self.kx != 1:           
            self.kx = -1
            self.ky = 0
            
        if keys[pygame.K_d] and self.kx != -1:
            self.kx = 1
            self.ky = 0
            
        if keys[pygame.K_w] and self.ky != 1:
            self.kx = 0
            self.ky = -1
            
        if keys[pygame.K_s] and self.ky != -1:
            self.kx = 0
            self.ky = 1
        self.x += (self.kx * self.speed) * dt / 100
        self.y += (self.ky * self.speed) * dt / 100
        

        if self.x < 0:
                self.x = SCREEN_WIDTH - self.width

        if self.x + self.width > SCREEN_WIDTH:
                self.x = 0

        if self.y > SCREEN_HEIGHT:
                self.y = 0
        
        if self.y < 0:
                self.y = SCREEN_HEIGHT


class Apple:
    def __init__(self, _x, _y,):
        self.x = _x
        self.y = _y
        self.radius = 15
        self.food = []

    def draw(self, screen):
        pygame.draw.circle(screen, ('orange'), (self.x, self.y), self.radius)
