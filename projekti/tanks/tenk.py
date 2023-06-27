import pygame
import math
SCREEN_HEIGHT=720
SCREEN_WIDTH=1280
pygame.mixer.init()
bullet_sound = pygame.mixer.Sound("./9mm-pistol-shot-6349.mp3")
class Tank:
    def __init__(self, _x, _speed, _width, _height, _alpha,k1,k2,k3,k4,k5):
        self.x = _x
        self.speed = _speed
        self.color = (50,50,20)
        self.width = _width
        self.height = _height
        self.bullets = []
        self.alpha=_alpha
        self.r=50
        self.firekey=k1
        self.leftkey=k2
        self.rightkey=k3
        self.upkey=k4
        self.downkey=k5
        self.health=100
        self.image = pygame.image.load("./edt.jpg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def draw(self, screen):
        
        rect = pygame.Rect(self.x, SCREEN_HEIGHT-150, self.width, self.height)
        
        pygame.draw.line(screen,self.color,(self.x + self.width/2,SCREEN_HEIGHT-150),(self.x + self.width/2+math.sin(self.alpha)*self.r,SCREEN_HEIGHT-160+math.cos(self.alpha)*self.r),5)

        screen.blit(self.image, (self.x, SCREEN_HEIGHT - 150))


    
    
    def update(self, keys, dt):
        
        keys = pygame.key.get_pressed()
        # Update pozicije po dugmicima
        #ovo treba prebaciti u tanks.py , i napraviti metode move
        if keys[self.leftkey]:
            self.x -= self.speed * dt
            if self.x < 0:
                self.x = 0
        if keys[self.rightkey]:
            self.x += self.speed * dt
            if self.x + self.width > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.width
        if keys[self.upkey]:
            self.alpha+=0.3*dt
        if keys[self.downkey]:
            self.alpha-=0.3*dt


        #TU POCINJE ZA TENK 2
        # if keys[pygame.K_LEFT]:
        #     self.x -= self.speed * dt
        #     if self.x < 0:
        #         self.x = 0
        # if keys[pygame.K_RIGHT]:
        #     self.x += self.speed * dt
        #     if self.x + self.width > SCREEN_WIDTH:
        #         self.x = SCREEN_WIDTH - self.width
        # if keys[pygame.K_UP]:
        #     self.alpha+=0.3*dt
        # if keys[pygame.K_DOWN]:
        #     self.alpha-=0.3*dt

    def fire(self, event):

        if (event.key == self.firekey):
            self.bullets.append(Bullet(self.x+self.width/2, SCREEN_HEIGHT-150, 30,25,self.alpha))
            bullet_sound.play()
          
class Bullet:

    def __init__(self, _x, _y, _speed_x, _speed_y,_alpha):
        self.alpha=_alpha-1.5
        self.x = _x
        self.y = _y
        self.speed_x = _speed_x*math.cos(self.alpha)
        self.speed_y = _speed_y*math.sin(self.alpha)
        self.radius = 5
        
    def update(self):  
        self.y -= self.speed_y 
        self.speed_y -= 0.08 * 9.81
        
        self.x += self.speed_x

    def draw(self, screen):
        pygame.draw.circle(screen, (20,20,20), (self.x, self.y), self.radius)