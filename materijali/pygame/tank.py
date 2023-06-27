import pygame

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

class Tank:
    def __init__(self, _x, _speed, _width, _height):
        self.x = _x
        self.speed = _speed
        self.color = (0,0,0)
        self.width = _width
        self.height = _height
        self.bullets = []

    def draw(self, screen):
        rect = pygame.Rect(self.x, SCREEN_HEIGHT-150, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)
    
    def update(self, keys, dt):
        # Update pozicije po dugmicima
        if keys[pygame.K_a]:
            self.x -= self.speed * dt / 100
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_d]:
            self.x += self.speed * dt / 100
            if self.x + self.width > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.width

        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.x+self.width/2, SCREEN_HEIGHT-150, 5,50))


class Bullet:
    def __init__(self, _x, _y, _speed_x, _speed_y):
        self.x = _x
        self.y = _y
        self.speed_x = _speed_x
        self.speed_y = _speed_y
        self.radius = 5

    def update(self):  
        self.y -= self.speed_y
        self.speed_y -= 0.1 * 9.81
        
        self.x += self.speed_x

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius)
