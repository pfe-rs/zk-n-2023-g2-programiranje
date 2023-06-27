import pygame

screenHeight = 800
screenWidth = 600

crna = (0, 0, 0)
narandzasta = (255, 153, 51)
a = 20
b = 20

image = pygame.image.load('assets/cvrle.png')
scale = 4
SIZE = (25 * scale, 19 * scale)
image = pygame.transform.scale(image, SIZE)

class Ptica:
    def __init__(self, _x, _y, _vsp, _radius, _gravity):
        self.x = _x
        self.y = _y
        self.vsp = _vsp
        self.color = (255,0,0)
        self.radius = _radius
        self.center = [self.x, self.y]
        self.gravity = _gravity

    def draw(self, screen):
        image.convert_alpha()
        #pygame.draw.polygon(screen, narandzasta, ((self.x + self.radius - 5, self.y - a / 2), (self.x + self.radius + b, self.y), (self.x + self.radius - 5, self.y + a / 2)))
        #pygame.draw.circle(screen, self.color, self.center, self.radius)
        #pygame.draw.circle(screen, crna, [self.x + self.radius / 2, self.y - self.radius / 3], self.radius / 4)
        screen.blit(image, (self.x - 19 * scale / 2, self.y - 19 * scale / 2))

    def update(self, dt):
        # Update pozicije po dugmicima
        self.y -= self.vsp * dt
        self.center[1] = self.y
        if self.y >= screenHeight - self.radius:
            self.y = screenHeight - self.radius
            self.center[1] = self.y
        elif self.y <= self.radius:
            self.y = self.radius
            self.center[1] = self.y

    def gravitacija(self, dt):
        self.y += self.gravity * dt
        self.center[1] = self.y

    def pao(self):
        return (bool)(self.y + self.radius > screenHeight)
    
    def prosao(self, stu):
        return (bool)(self.x == stu.x + self.radius * 2)

