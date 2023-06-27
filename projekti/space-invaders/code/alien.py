import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self,color,x,y):
        super().__init__()
        
        if color == 'red' :
            file_path = 'ssets/po.png'
            self.value = 100

        if color == 'yellow' :
            file_path = 'ssets/yellow.png'
            self.value = 300

        if color == 'green':
            file_path = 'ssets/green.png'
            self.value = 200

        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
    def update(self,direction):
        self.rect.x += direction ## nismo fanovi one direction treba 2

class Extra(pygame.sprite.Sprite):

    def __init__(self,side,screen_width):
        super().__init__()
        
        self.image = pygame.image.load('ssets/pink.png').convert_alpha()
        
        if side == 'right':
            x= screen_width + 50
            self.speed = -3
        else:
            x=-50
            self.speed = 3
        self.rect = self.image.get_rect(topleft = (x,10))
      

    def update(self):
        self.rect.x += self.speed 
        