import pygame
from ptica import Ptica
import math

screenHeight = 800
screenWidth = 600

class Stub:
    def __init__(self, _x, _y, _a, _b, _boja, _outline):
        self.x = _x
        self.y = _y
        self.a = _a
        self.b = _b
        self.a1 = self.y - self.a / 2
        self.a2 = screenHeight - self.a - self.y + self.a / 2
        self.color = _boja
        self.outline = _outline
        self.gotov = False

    def draw(self, screen):
        width = 4
        #region gornji
        rect1 = pygame.Rect(self.x - self.b / 2, 0, self.b, self.a1)
        pygame.draw.rect(screen, self.color, rect1)
        pygame.draw.line(screen, self.outline, (self.x - self.b / 2, 0), (self.x - self.b / 2, self.y - self.a / 2 + width / 2), width)
        pygame.draw.line(screen, self.outline, (self.x + self.b / 2, 0), (self.x + self.b / 2, self.y - self.a / 2 + width / 2), width)
        pygame.draw.line(screen, self.outline, (self.x - self.b / 2, self.y - self.a / 2), (self.x + self.b / 2, self.y - self.a / 2), width)
        #endregion

        #region donji
        rect2 = pygame.Rect(self.x - self.b / 2, self.y + self.a / 2, self.b, self.a2)
        pygame.draw.rect(screen, self.color, rect2)        
        pygame.draw.line(screen, self.outline, (self.x - self.b / 2, screenHeight), (self.x - self.b / 2, self.y + self.a / 2 - 1), width)
        pygame.draw.line(screen, self.outline, (self.x + self.b / 2, screenHeight), (self.x + self.b / 2, self.y + self.a / 2 - 1), width)
        pygame.draw.line(screen, self.outline, (self.x - self.b / 2, self.y + self.a / 2), (self.x + self.b / 2, self.y + self.a / 2), width)
        #endregion
    def pomeri(self, hsp):
        self.x -= hsp

    def nestao(self):
        return (bool)(self.x + self.b / 2 < 0)



        

       
    

