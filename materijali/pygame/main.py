import pygame
from tank import Tank, Bullet
from collision import collision
import random

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pfe = (50, 200, 200)
pod = pygame.Rect(0, SCREEN_HEIGHT-100, SCREEN_WIDTH, 100)

tank = Tank(50, 100, 100, 50)

while running:
    screen.fill(pfe)
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys=pygame.key.get_pressed()
    
    pygame.draw.rect(screen, (100,100,0), pod)
    tank.draw(screen)
    tank.update(keys, dt)

    random_x_speed = random.randint(-50, 50)*0.1

    
    for bullet in tank.bullets:
        bullet.update()
        bullet.draw(screen)
        if collision(tank.x, SCREEN_HEIGHT-100-tank.height, tank.width, tank.height, bullet.x, bullet.y, bullet.radius):
            print("GAME OVER")
            while True:
                pass

    pygame.display.flip()
