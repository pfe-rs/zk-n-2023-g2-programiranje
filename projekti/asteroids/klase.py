import pygame as pg
import random
import math

sirina=1280
visina=720
cooldown_tracker = 0
    
class Igrac:
    def __init__(self,x,y,speed,pfe):
        self.x=x
        self.y=y
        self.speed=speed
        self.sirinapfe=pfe.get_rect().width
        self.visinapfe=pfe.get_rect().height
        self.pfe=pg.transform.scale(pfe, (self.sirinapfe/2, self.visinapfe/2))
        self.bullets=[]
        
    def draw(self,prozor):
        prozor.blit(self.pfe, (self.x,self.y))
        
   
    def update(self, keys, dt,clock):
        global cooldown_tracker
        cooldown_tracker += clock.get_time()
        if cooldown_tracker > 300:
            cooldown_tracker = 0

        for bullet in self.bullets:
            if(bullet.y>visina or bullet.y<0 or bullet.x>sirina or bullet.x<0):
                self.bullets.pop(self.bullets.index(bullet))

        if keys[pg.K_a]:
            self.x -= self.speed * dt / 400
            if self.x < 0:
                self.x = 0
            
            if (keys[pg.K_SPACE] and keys[pg.K_d]):
              pass
            elif(keys[pg.K_SPACE] and keys[pg.K_w] and cooldown_tracker == 0):
                    self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, -50, -50))
            elif(keys[pg.K_SPACE] and keys[pg.K_s] and cooldown_tracker == 0):
                    self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, -50, 50))
            elif (keys[pg.K_SPACE] and cooldown_tracker == 0):
                    self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, -50, 0))
                
        if keys[pg.K_d]:
            self.x += self.speed * dt / 400
            if self.x + self.sirinapfe/2 > sirina:
                self.x = sirina - self.sirinapfe/2

            if (keys[pg.K_SPACE] and keys[pg.K_a]):
                pass
            elif (keys[pg.K_SPACE] and keys[pg.K_w] and cooldown_tracker == 0):
                self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 50, -50))
            elif (keys[pg.K_SPACE] and keys[pg.K_s] and cooldown_tracker == 0):
                self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 50, 50))
            elif (keys[pg.K_SPACE] and cooldown_tracker == 0):
                self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 50, 0))
                
        if keys[pg.K_w]:
            self.y -= self.speed * dt / 400
            if self.y<0:
                self.y=0

            if (keys[pg.K_SPACE] and keys[pg.K_s]):
              pass
            elif(keys[pg.K_SPACE] and keys[pg.K_a]):
                pass
            elif(keys[pg.K_SPACE] and keys[pg.K_d]):
                pass
            elif (keys[pg.K_SPACE] and cooldown_tracker == 0):
                self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 0,-50))
                    
        if keys[pg.K_s]:
            self.y += self.speed * dt / 400
            if self.y + self.visinapfe/2 > visina:
                self.y = visina - self.visinapfe/2
            
            if (keys[pg.K_SPACE] and keys[pg.K_w]):
                pass
            elif(keys[pg.K_SPACE] and keys[pg.K_a]):
                pass
            elif(keys[pg.K_SPACE] and keys[pg.K_d]):
                pass
            elif (keys[pg.K_SPACE] and cooldown_tracker == 0):
                self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 0, 50))
        if (keys[pg.K_SPACE] and keys[pg.K_a]==0 and keys[pg.K_w]==0 and keys[pg.K_d]==0 and keys[pg.K_s]==0 and cooldown_tracker == 0):
            self.bullets.append(Bullet(self.x+self.sirinapfe/4, self.y+self.visinapfe/4, 0,-50))
class Bullet:
    def __init__(self, x, y,speed_x,speed_y):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.radius = 5

    def update(self,dt):
        self.x += self.speed_x * dt/50
        self.y += self.speed_y * dt/50
    
    def draw(self, screen):
        pg.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius)
class Asteroid:
    def __init__(self,asteroid):
        self.x=random.choice([-300, 1580])
        self.y=random.randint(-100,820)
        if (self.y<visina/2 and self.x==-300):
            self.speedx=random.randint(10,50)
            self.speedy=random.randint(10,50)
        if (self.y>visina/2 and self.x==-300):
            self.speedx=random.randint(10,50)
            self.speedy=random.randint(-50,-10)
        if (self.y<visina/2 and self.x==1580):
            self.speedx=random.randint(-50,-10)
            self.speedy=random.randint(10,50)
        if (self.y>visina/2 and self.x==1580):
            self.speedx=random.randint(-50,-10)
            self.speedy=random.randint(-50,-10)
        self.sirinaasteroid=asteroid.get_rect().width
        self.visinaasteroid=asteroid.get_rect().height
        self.radius=random.randrange(2,10,2)
        self.asteroid=pg.transform.scale(asteroid, (self.sirinaasteroid*2/self.radius, self.visinaasteroid*2/self.radius))
    
    
    def draw (self,prozor):
        prozor.blit(self.asteroid, (self.x,self.y))
        
    def update (self,dt):
        self.x+=self.speedx*dt/100
        self.y+=self.speedy*dt/100
    
    
