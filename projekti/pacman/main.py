import pygame
import time
from pygame import mixer
from collision import *
from walls import *
from hyperparameters import *
from Pacman import *
from coin import *


wall_color = (118, 190, 151)
pacman_color = (255, 255, 0)
speed = 2
pacman_radius = 1.99
pacman_start_x = SCALE_FACTOR*2
pacman_start_y = SCALE_FACTOR*2
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("Pac-Man")
running = True
clock = pygame.time.Clock()

mixer.init()
mixer.music.load("./pacman theme.wav")
mixer.music.play()

pacman_sprite_path = "./pfe.webp"
pacman_sprite = pygame.image.load(pacman_sprite_path)

pacman = Pacman(pacman_start_x, pacman_start_y, pacman_radius, pacman_color, speed, 1, pacman_sprite)

coin_sound = pygame.mixer.Sound("./pacman_chomp.wav")

t_end = time.time()+4.5
while(time.time() < t_end):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    screen.fill("black")
    for wall in walls:
        pygame.draw.rect(screen, wall_color, wall)
    for c in coins:
        c.draw(screen)
    pacman.draw(screen)

    pygame.display.flip()

points = 0

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(points).encode("utf-8").decode("utf-8"), True, (255, 200, 200))
text_rect = text.get_rect()
text_rect.center = (100, 100)

while(running):
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    for wall in walls:
        pygame.draw.rect(screen, wall_color, wall)
    
    for c in coins:
        c.draw(screen)
    for c in coins:
        if(collision(pacman.pos_x, pacman.pos_y, pacman.radius, pacman.radius, c.pos_x, c.pos_y, c.radius)):
            points += 10
            pygame.mixer.Sound.play(coin_sound)
            coins.remove(c)

    text = font.render(str(points).encode("utf-8").decode("utf-8"), True, (255, 200, 200))
    screen.blit(text, text_rect)

    if(len(coins) == 0):
        running = False

    keys = pygame.key.get_pressed()
    pacman.update(keys)
    pacman.draw(screen)

    pygame.display.flip()


pygame.quit()