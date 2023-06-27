import pygame
from button import Button
from jedna_zaba import jedna_zaba



def jedna_igra():
    screen_height = 720
    screen_width = 1280
    screen_color = (16, 180, 201)
    screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA)

    #koliko zaba je premesteno
    zaba_count = 0
    #zivoti
    lives = 5
    
    kucice = list(range(100, screen_width - 100, 250))
    popunjene_kucice = []

    button_width = 200
    button_height = 90

    running1 = True
    running = False

    #kreiranej dugmeta
    start = Button((screen_width - button_width)  // 2, 3 * (screen_height - button_height) // 4, button_width, button_height, "START GAME", (0, 0, 0), (255, 255, 255))
    
    #slike
    screen = pygame.display.set_mode((screen_width, screen_height))
    logo = pygame.image.load("frogger_logoo.png").convert_alpha()
    logo = pygame.transform.scale(logo, (screen_width, screen_height // 2))
    logo.set_colorkey((0, 0, 0))
    screen_picture = pygame.image.load("pozadina.png").convert()
    
    #provera da li je kliknuto sugme ili x 
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                running = True
                return 0, 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start.is_clicked(pygame.mouse.get_pos()):
                    running = True
                 
        screen.blit(screen_picture, (0, 0))
        screen.blit(logo, (0, 0))
        start.draw(screen)
        
        pygame.display.flip()

    #pozivanje funkcije jedna_zaba() dok ima dovoljno zivota ili dok nisu sve kucice popunjene
    while lives > 0 and zaba_count < 5 and running1:
        lives, zaba_count, kucice, popunjene_kucice = jedna_zaba(lives, zaba_count, kucice, popunjene_kucice)

    #da li su izgubljeni svi zivoti
    if lives <= 0:
        return False, "GAME OVER"

    #da li su sve zabe premestene
    elif zaba_count == 5:
        return False, "WIN"
