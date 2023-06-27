import pygame as pg
SCREEN_DIMENTION = 512

class Car:
    def __init__(self, color, speed, startX, startY):
        self.color = color
        self.speed = speed/1000
        self.sprite = pg.Rect(startX, startY, 32, 16)
        
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.sprite)
    
    def move(self, targetX, targetY):
        movX = targetX-self.sprite.left
        movY = targetY-self.sprite.top
        self.sprite.left += movX * self.speed
        self.sprite.top += movY * self.speed
        
        