import pygame
from tenk import Tank,Bullet
from sudar import sudaren
from kraj_igre import game_over
SCREEN_HEIGHT=720
SCREEN_WIDTH=1280
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
pygame.init()
pygame.display.set_caption("Tanks 2v2")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
bojapozadine=(80,150,250)
pod=pygame.Rect(0,SCREEN_HEIGHT-100,SCREEN_WIDTH,100)

def draw_health_bars(screen, tank1, tank2):
 
    tank1_health_bar_width = tank1.health * 2
    tank2_health_bar_width = tank2.health * 2

    tank1_health_bar_rect = pygame.Rect(10, 10, tank1_health_bar_width, 10)
    tank2_health_bar_rect = pygame.Rect(10, 30, tank2_health_bar_width, 10)

    
    pygame.draw.rect(screen, GREEN, tank1_health_bar_rect)
    pygame.draw.rect(screen, GREEN, tank2_health_bar_rect)

    
    if tank1.health <= 30:
        pygame.draw.rect(screen, YELLOW, tank1_health_bar_rect)
    if tank1.health <= 10:
        pygame.draw.rect(screen, RED, tank1_health_bar_rect)

    if tank2.health <= 30:
        pygame.draw.rect(screen, YELLOW, tank2_health_bar_rect)
    if tank2.health <= 10:
        pygame.draw.rect(screen, RED, tank2_health_bar_rect)

tenk=Tank(1180,200,100,50,3.10,pygame.K_PERIOD,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_UP)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
tenk2=Tank(0,200,100,50,3.10,pygame.K_SPACE,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
while running: 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            tenk.fire(event)
            tenk2.fire(event)

    screen.fill(bojapozadine)
    draw_health_bars(screen, tenk, tenk2)
    pygame.draw.rect(screen,(150,150,20),pod)
    pygame.draw.ellipse(screen, pygame.Color("yellow"), (80, 90, 80, 80))
    pygame.draw.ellipse(screen, pygame.Color("white"), (700, 80, 140, 80))
    pygame.draw.ellipse(screen, pygame.Color("white"), (900, 160, 120, 70))
    pygame.draw.ellipse(screen, pygame.Color("white"), (260, 140, 160, 70))
    pygame.draw.ellipse(screen, pygame.Color("white"), (460, 140, 100, 70))
    tenk.draw(screen)
    tenk2.draw(screen)
    keys = pygame.key.get_pressed()
    keys2=pygame.key.get_pressed()
    
    tenk.update(keys,dt)
    tenk2.update(keys2,dt) 
    
    for bullet in tenk.bullets+tenk2.bullets:
        bullet.update()
        bullet.draw(screen)
        if sudaren(tenk.x,SCREEN_HEIGHT-100-tenk.height,tenk.width,tenk.height,bullet.x,bullet.y,bullet.radius):
            if bullet in tenk.bullets:
                tenk.bullets.remove(bullet)
            else:
                tenk2.bullets.remove(bullet)
            tenk.health=tenk.health-20
            # while True:    
            #     pass
        if sudaren(tenk2.x,SCREEN_HEIGHT-100-tenk2.height,tenk2.width,tenk2.height,bullet.x,bullet.y,bullet.radius):
            if bullet in tenk2.bullets:
                tenk2.bullets.remove(bullet)
            else:
                tenk.bullets.remove(bullet)
            tenk2.health=tenk2.health-20
            # while True:
            #     pass
        
    # for bullet in tenk2.bullets+tenk.bullets:
    #     bullet.update()
    #     bullet.draw(screen)
        
    if tenk2.health==0:
        game_over()
        tenk2.health=100
        tenk.health=100
        for bullet in tenk.bullets:
            tenk.bullets.remove(bullet)
            
    if tenk.health==0:
        game_over()
        tenk.health=100
        tenk2.health=100
        for bullet in tenk.bullets:
            tenk.bullets.remove(bullet)
            

    pygame.display.flip()
    dt = clock.tick(50)/1000
pygame.mixer.quit()
pygame.quit()



