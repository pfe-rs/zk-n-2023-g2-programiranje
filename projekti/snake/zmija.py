import pygame
import shelve
from zmija_class import Zmija, Apple
from collison import collision
import random

score = 1
high_score_1 = ['0']
shifle = shelve.open("high_score.txt")
if 'highScore' not in shifle:
    shifle['highScore'] = '0'

#shifle.close()

#high_score = shelve.open("high_score.txt")

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_img = pygame.image.load('tileable_grass.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True

snake_x = SCREEN_WIDTH//2
snake_y = SCREEN_HEIGHT//2
x_apple = random.randint(0, SCREEN_WIDTH)
y_apple = random.randint(0, SCREEN_HEIGHT)
zmija = Zmija(snake_x, snake_y, 30, 50, 50)
apple = Apple(x_apple, y_apple)
font = pygame.font.Font(None, 36)
cnt = 0
'''
def collision_snake(zmija_list):
    for i in zmija_list:
        for j in range(1,len(zmija_list)):
            if zmija_list[i][0][0] == zmija_list[j][0][0] or zmija_list[i][0][1] == zmija_list[j][0][1]:
                return True
    return False
'''

while running:
    screen.fill('#134b0f')
    dt = clock.tick(60)
    screen.blit(bg_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
             running = False


    
    zmija.draw(screen)
    zmija.update(keys, dt)
    apple.draw(screen)
    score_text = font.render(f'Score: {score-1}', True, (255, 255, 255))
    screen.blit(score_text, (10, 40))
    higher_score = shifle['highScore']
    high_score_text = font.render(f'High score: {higher_score}', True, (255, 255, 255))
    screen.blit(high_score_text, (10 ,10))

    if cnt == 3:
        cnt = 0

        if(score > zmija.size):
            Zmija.zmija_list.insert(0, (zmija.x, zmija.y))
            zmija.size += 1

        i=score-1
    
        while(i>0):
            Zmija.zmija_list[i] = Zmija.zmija_list[i-1]
            i -= 1
        Zmija.zmija_list[0]=(zmija.x, zmija.y)
    cnt += 1

    for i in range(zmija.size):
        zmija.draw_i(screen,i)

    if collision(zmija.x, zmija.y, zmija.width, zmija.height, apple.x, apple.y, apple.radius):
        score += 1

        x_apple = random.randint(60, SCREEN_WIDTH - 100)
        y_apple = random.randint(60, SCREEN_HEIGHT- 100)
        apple = Apple(x_apple, y_apple)
        apple.draw(screen)
    #if collision_snake(zmija.zmija_list):
        #running = False


    pygame.display.flip()
if int(shifle['highScore']) < (score - 1):  
    shifle['highScore'] = str(score-1)
shifle.close()

#napraviti da zmija ne moze sama da se pojede
