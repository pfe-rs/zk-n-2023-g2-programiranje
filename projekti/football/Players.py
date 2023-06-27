import pygame
import math

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

class Player1:
    def __init__(self, _x, _y, _speed, _width, _height):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.color = (0,0,0)
        self.height = _height
        self.width = _width
     

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

    def update(self, keys, dt):
        # Update pozicije po dugmicima
        if keys[pygame.K_w]:
            self.y -= self.speed * dt / 100
            if self.y < 100:
                self.y = 100
        if keys[pygame.K_s]:
            self.y += self.speed * dt / 100
            if self.y + self.height > 700:
                self.y = 700 - self.height

class Player2:
    def __init__(self, _x, _y, _speed, _width, _height):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.color = (0,0,0)
        self.height = _height
        self.width = _width
     

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

    def update(self, keys, dt):
        # Update pozicije po dugmicima
        if keys[pygame.K_UP]:
            self.y -= self.speed * dt / 100
            if self.y < 100:
                self.y = 100
        if keys[pygame.K_DOWN]:
            self.y += self.speed * dt / 100
            if self.y + self.height > 700:
                self.y = 700 - self.height        


class Ball:
    def __init__(self, _x, _y, _speed):
        self.x = _x
        self.y = _y
        self.speed_x = _speed
        self.speed_y = _speed
        self.radius = 30
  

    def update(self):  
        self.y += self.speed_y
        self.x += self.speed_x



    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius)
