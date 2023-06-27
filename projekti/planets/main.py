import pygame
from objects import Planet, Scroll
import collision

SCREEN_HEIGHT = 950
SCREEN_WIDTH = 1800
counter = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
planets = []
back_c = (50, 150, 125)

scroll = Scroll(30, 30)
for i in range(300):  
    planets.append(Planet())



while running:
    screen.fill(back_c)
    dt = clock.tick(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vx = -planets[counter%len(planets)].x + SCREEN_WIDTH/2
                vy = -planets[counter%len(planets)].y + SCREEN_HEIGHT/2
                for i in planets:
                    i.x += vx
                    i.y += vy
                counter += 1
            if event.key == pygame.K_LEFT:
                vx = -planets[counter%len(planets)].x + SCREEN_WIDTH/2
                vy = -planets[counter%len(planets)].y + SCREEN_HEIGHT/2
                for i in planets:
                    i.x += vx
                    i.y += vy
                counter -= 1
            if event.key == pygame.K_r:
                planets.clear()
                for i in range(300):
                    planets.append(Planet())

        
    keys=pygame.key.get_pressed()

    for i in planets:
        i.draw(screen)
        i.move()
        i.update(planets,dt)
    to_remove = []
    for i in planets:
        for j in planets:
            if i == j: continue
            if collision.circcoll(i.x, i.y, i.r, j.x, j.y, j.r):
                if not (i in to_remove) and not (j in to_remove):
                    if(i.r >= j.r):
                        to_remove.append(j)
                        i.mass += j.mass
                        if i.mass > 70000000000:
                            i.mass = 70000000000
                        i.r += j.r*(j.mass/i.mass)*0.2
                        if i.r > 320:
                            i.r = 320
                        continue
                    if(j.r > i.r):
                        to_remove.append(i)
                        j.mass += i.mass
                        if j.mass > 70000000000:
                            j.mass = 70000000000
                        j.r += i.r*(i.mass/j.mass)*0.2
                        if j.r > 320:
                            j.r = 320
    for i in to_remove:
        planets.remove(i)
    scroll.update(keys, planets)
    pygame.display.flip()
