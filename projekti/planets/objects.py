import pygame
import random
import math
# piksel 100km
SCREEN_HEIGHT = 950
SCREEN_WIDTH = 1800

class Scroll:
    def __init__(self, speedx, speedy):
        self.x = speedx
        self.y = speedy
        self.counter = 0
    
    def update(self, keys, planets):
        # Update pozicije po dugmicima
        vx = 0
        vy = 0
        if len(keys) == 0: return
        if keys[pygame.K_a]:
            vx = self.x
        if keys[pygame.K_d]:
            vx = -self.x
        
        if keys[pygame.K_w]:
            vy = self.y

        if keys[pygame.K_s]:
            vy = -self.y
        for i in planets:
            i.x += vx
            i.y += vy    

class Planet:
    def __init__(self):
        self.r = random.randint(5, 23)
        self.x = random.randint(0,SCREEN_WIDTH)
        self.y = random.randint(0,SCREEN_HEIGHT)
        self.vx = random.randint(-80, 80)*0.01
        self.vy = random.randint(-80, 80)*0.01
        self.mass = self.r*self.r*self.r*math.pi*random.randint(500, 7500)*4/3
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def update(self, planets,dt):
        for planet in planets:
            if(planet == self): continue
            Y = planet.y - self.y
            X = planet.x - self.x
            d = math.sqrt(X*X + Y*Y)
            cos = X/d
            sin = Y/d
            F = ((planet.mass)/(d*d))*9.6743*math.pow(10,-10)*dt
            self.vx += cos*F
            self.vy += sin*F        
    def move(self):
        self.x += self.vx
        self.y += self.vy

    
