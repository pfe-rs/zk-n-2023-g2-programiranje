import pygame
from button import Button
from jedna_igra import jedna_igra
from pygame.locals import *

screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA)
button_width = 200
button_height = 90

#dugme za ponovno pokretanje igre
button_nastavi = Button(2 * (screen_width - button_width) // 6, 8 * (screen_height - button_height) // 9, button_width, 
                        button_height, "RESTART", (0, 0, 0), (255, 255, 255))
#dugme za prekidanje igre
button_zaustavi = Button(4 * (screen_width - button_width) // 6, 8 * (screen_height - button_height) // 9, button_width, 
                         button_height, "QUIT", (0, 0, 0), (255, 255, 255))

running = False
running1 = False

#slike
logo = pygame.image.load("frogger_logoo.png").convert_alpha()
logo = pygame.transform.scale(logo, (screen_width, screen_height // 2))
logo.set_colorkey((0, 0, 0))
over = pygame.image.load("over1.png").convert()
over = pygame.transform.scale(over, (700, 260))
over.set_colorkey((0, 0, 0))
win = pygame.image.load("win1.png").convert()
win = pygame.transform.scale(win, (400, 200))
win.set_colorkey((0, 0, 0))
screen_picture = pygame.image.load("pozadina.png").convert()

while not running:
    
    running1 = False
    running, ispis = jedna_igra()
    
    while not running1 and not running:
        running1 = False
        screen.blit(screen_picture, (0, 0))
        #koji je rezultat prethodne igre
        if ispis == "WIN":
            screen.blit(win, (screen_width // 2 - 200, 3 * screen_height // 5 - 90))
        elif ispis == "GAME OVER":
            screen.blit(over, (screen_width // 2 - 400, 3 * screen_height // 5 - 90))
        else:
            running = True
            break
        
        #iscrtavanje
        screen.blit(logo, (0, 0))
        button_nastavi.draw(screen)
        button_zaustavi.draw(screen)

        #da li je kliknuto x, restart ili quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = True
                running = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_nastavi.is_clicked(pygame.mouse.get_pos()):
                    running = False
                    running1 = True 
                    break
                if button_zaustavi.is_clicked(pygame.mouse.get_pos()):
                    running = True
        
        pygame.display.flip()
