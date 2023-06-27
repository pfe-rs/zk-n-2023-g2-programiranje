import pygame
import math

from kolizija import kolizija
from Players import Player1
from Players import Player2
from Players import Ball

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

pozadina = (1,50,32)
teren = pygame.Rect(212, 100, 900, 600)
gol1 = pygame.Rect(206, 300, 10, 200)
gol2 = pygame.Rect(1110, 300, 10, 200)
dt = clock.tick(60)


player1 = Player1(320, 400, 60, 20, 130)
player2 = Player2(990, 400, 60, 20, 130)
ball = Ball(300, 300, 7)
    
player1_goals = 0
player2_goals = 0

terenslika = pygame.image.load('./teren.jpg')
terenslika = pygame.transform.scale(terenslika, (900, 600))

while running:

    screen.fill(pozadina)
    screen.blit(terenslika,(212,100))
    dt = clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    font = pygame.font.Font(None, 36)

    keys=pygame.key.get_pressed()
    
    score_text = font.render(f'PLAYER 1     {player1_goals}        -        {player2_goals}     PLAYER 2', True, (255, 255, 255))   
    screen.blit(score_text , (433, 40))

   # pygame.draw.rect(screen, (126,175,52), teren) - ovo ako nece da ucita sliku terena
    pygame.draw.rect(screen, (255,255,255), gol1)
    pygame.draw.rect(screen, (255,255,255), gol2)
  
    player1.draw(screen)
    player1.update(keys, dt)

    player2.draw(screen)
    player2.update(keys, dt)

    ball.draw(screen)
    ball.update()

    #sa igracima
    if kolizija(player1.x, player1.y, player1.width, player1.height, ball.x, ball.y,  ball.radius):
       ball.speed_x = ball.speed_x * (-1) 

    if kolizija(player2.x, player2.y, player2.width, player2.height, ball.x, ball.y,  ball.radius):        
        ball.speed_x = ball.speed_x * (-1)
        
#    if kolizija(player1.x, player1.y, player1.width, player1.height, ball.x, ball.y,  ball.radius):
    #    if((ball.y + ball.radius == player1.y or ball.y - ball.radius == player1.y) and (ball.x >= player1.x and ball.x <= player1.x + 20)):
    #        ball.speed_y = ball.speed_y * (-1)
     #   else:
      #      ball.speed_x = ball.speed_x * (-1) #ovo sam pokusala nesto sa smerom ali iz nekog razloga nece, nebitno

    #sa zidovima

    #levi i desni
    if (ball.x + ball.radius >= 1112 or ball.x - ball.radius <= 212):
        ball.speed_x = ball.speed_x * (-1)

    #gore i dole
    if (ball.y+ ball.radius >= 700 or ball.y - ball.radius <= 100):
        ball.speed_y = ball.speed_y * (-1)
            

    #golovi
    if (ball.x + ball.radius >= 1112 and ball.y > 300 and ball.y < 500):
        player1_goals = player1_goals + 1
   

    if (ball.x - ball.radius <= 212 and ball.y > 300 and ball.y < 500):
        player2_goals = player2_goals + 1
  


    pygame.display.flip()
