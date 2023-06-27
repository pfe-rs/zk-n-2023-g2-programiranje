import pygame as pg
from klase import Igrac,Bullet,Asteroid
import math

pg.init()
sirina=1280
visina=720
prozor=pg.display.set_mode((sirina,visina))
pg.display.set_caption('Asteroidi')
pozadina=pg.image.load("svemir.jpg").convert()
pfe = pg.image.load('pfe.png').convert_alpha()
asteroidslika= pg.image.load('asteroid.png').convert_alpha()
running=True
clock=pg.time.Clock()
igrac=Igrac(608,328,150,pfe)
asteroid=Asteroid(asteroidslika)
asteroids = [Asteroid(asteroidslika) for _ in range(7)]
metak=Bullet(608,328,0,0)
counter = 0 
score=0
fontgameover=pg.font.SysFont("Gill Sans", 200)
gameover=fontgameover.render('GAME OVER!', True, (218, 231, 246))
gameoverRect=gameover.get_rect()
gameoverRect.center=(640,300)
fontrestart=pg.font.SysFont("Gill Sans", 50)
restart=fontrestart.render('Press r to restart', True, (218, 231, 246))
restartRect=restart.get_rect()
restartRect.center=(640,450)
quit=fontrestart.render('Press q to quit', True, (218, 231, 246))
quitRect=quit.get_rect()
quitRect.center=(640,500)
font = pg.font.SysFont("Cooper black", 32)
text = font.render('SCORE:', True, (218, 231, 246))
textRect = text.get_rect()
textRect.center = (70, 30)
scoretext=font.render(str(score),True,(218, 231, 246))
scoretextRect = scoretext.get_rect()
scoretextRect.center = (140, 30)
play=fontrestart.render('Press p to play', True,(218, 231, 246))
playRect=play.get_rect()
playRect.center=(640,450)
pg.font.get_fonts()

def collision(rleft, rtop, rwidth, height, center_x, center_y, radius): 

    rright, rbottom = rleft + rwidth/2, rtop + height/2
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False  
    for x in (rleft, rleft+rwidth):
        for y in (rtop, rtop+height):
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True   
    return False

def collision1(centarx1,centary1,radius1,centarx2,centary2,radius2):
    if((radius1+radius2)>math.sqrt((centarx1-centarx2)*(centarx1-centarx2)+(centary1-centary2)*(centary1-centary2) or (radius1+radius2)>math.sqrt((centarx2-centarx1)*(centarx2-centarx1)+(centary2-centary1)*(centary2-centary1)))):
        return True
    else:
        return False 
        
while running:
    pg.display.flip()
    dt=clock.tick(500)
    prozor.blit(pozadina, (0,0))
    prozor.blit(text, textRect)
    scoretext=font.render(str(score),True,(255, 255, 255))
    prozor.blit(scoretext,scoretextRect)
    for event in pg.event.get():
        if event.type==pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running=False
    keys=pg.key.get_pressed()
    igrac.draw(prozor)
    igrac.update(keys, dt, clock)
    for bullet in igrac.bullets:
        for asteroid in asteroids:
            if collision1(bullet.x,bullet.y,bullet.radius,asteroid.x+(asteroid.sirinaasteroid*2/asteroid.radius)/2,asteroid.y+(asteroid.sirinaasteroid*2/asteroid.radius)/2,(asteroid.sirinaasteroid*2/asteroid.radius)/2):
                igrac.bullets.pop(igrac.bullets.index(bullet))
                asteroids.pop(asteroids.index(asteroid))
                if (asteroid.radius==2):
                    score+=5
                if (asteroid.radius==4):
                    score+=10
                if (asteroid.radius==6):
                    score+=20
                if (asteroid.radius==8):
                    score+=50
                if (asteroid.radius==10):
                    score+=100
        bullet.update(dt)
        bullet.draw(prozor)
    for asteroid in asteroids:
        asteroid.update(dt)
        asteroid.draw(prozor)
        if(asteroid.y>1020 or asteroid.y<-300 or asteroid.x>1780 or asteroid.x<-500 ):
                asteroids.pop(asteroids.index(asteroid))
        if collision(igrac.x, igrac.y, igrac.sirinapfe/2, igrac.visinapfe/2, asteroid.x+(asteroid.sirinaasteroid*2/asteroid.radius)/2, asteroid.y+(asteroid.sirinaasteroid*2/asteroid.radius)/2, (asteroid.sirinaasteroid*2/asteroid.radius)/2):
            pg.event.clear()
            for i in asteroids:
                asteroids.pop(asteroids.index(i))
            for bullet in igrac.bullets:
                igrac.bullets.pop(igrac.bullets.index(bullet))
            igrac=Igrac(608,328,150,pfe)
            score=0
            while True:
                prozor.blit(gameover, gameoverRect)
                prozor.blit(restart, restartRect)
                prozor.blit(quit, quitRect)
                pg.display.flip()
                event=pg.event.wait()
                if (event.type == pg.KEYDOWN and event.key == pg.K_r):
                    break 
                elif(event.type == pg.KEYDOWN and event.key == pg.K_q or event.type==pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                    pg.quit() 
    if counter == 100:
        asteroids.append(Asteroid(asteroidslika))
        counter = 0
    counter += 1
    #ds   sd       dddddddds dadawasssssdddawddwddddddddddddd