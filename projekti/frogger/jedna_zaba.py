import pygame
from karakteri import Frog, Caracter, Prepreka
import random



def jedna_zaba(zivoti, zaba_counti, kucice, popunjene_kucice):
    pygame.init()
    pygame.display.set_caption('Frogger')
    screen_height = 720
    screen_width = 1280  
    screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SRCALPHA)
    
    running = False
    clock = pygame.time.Clock()
    
    path_color= (107, 56, 39)
    screen_color = (16, 180, 201)

    pomeraj_x = 60
    pomeraj_y = 60
    y_pozicija = screen_height - 50

    #zaba, objekat
    zaba = Frog(x_pozicija=(screen_width - 50) // 2, y_pozicija=y_pozicija, x_dimenzija=50, y_dimenzija=50, boja=(137, 173, 19))

    #lista prepreka
    dinos = [[]] * 8

    #vreme izmedju pomeraja
    vreme = 0
    max_vreme = 35

    running1 = True

    imp = pygame.image.load("livess.png").convert_alpha()
    scaled_image = pygame.transform.scale(imp, (50, 50))
    screen_picture = pygame.image.load("pozadina.png").convert()
    kucica_puna = pygame.image.load("puna.png").convert_alpha()
    kucica_puna = pygame.transform.scale(kucica_puna, (80, 80))
    kucica_prazna = pygame.image.load("prazna.png").convert_alpha()
    kucica_prazna = pygame.transform.scale(kucica_prazna, (80, 80))

    #staze
    putevi = list(range(screen_height - 2 * zaba.duzina - 10, screen_height // 2, - pomeraj_x)) + list(range(screen_height // 2 - 10 - 2 * zaba.duzina, 10 + 2 * zaba.duzina, - pomeraj_x))
    path = []
    for y in putevi:
        rect = pygame.Rect(0, y, screen_width, 60)
        pygame.draw.rect(screen, path_color, rect)
        path.append(rect)

    
    #stanja za prepreke
    stanja = []        
    brz = [x for x in range(-18, 19) if abs(x) > 10]
    for i in range(8):
        polozaj, brzina, dimenx = random.randint(380, 480), random.choice(brz), random.randint(100, 240)
        a = [polozaj, brzina, dimenx]
        stanja.append(a)

    #inicijalne prepreke
    for j in range(8):
        for i in range(screen_width // (stanja[j][0] + stanja[j][2]) + 1):
            pozy = putevi[j]
            brzi = stanja[j][1]
            lista=["0", "1", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            boja = "#"
            for u in range(6):
                boja += random.choice(lista)
                if brzi > 0:
                    pozx = i * (stanja[j][0] + stanja[j][2]) 
                else:
                    pozx = i * (stanja[j][0] + stanja[j][2])
            dimenx = stanja[j][2]
            objekat = Prepreka(x_pozicija=pozx, y_pozicija=pozy, brzina=brzi, x_dimenzija=dimenx, y_dimenzija=pomeraj_x - 10, boja=boja)
            dinos[j].append(objekat)
 

    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                return 30, 30, 0, 0
            
        #iscrtavanje svih objekata na ekranu osim zabe i prepreka
        screen.blit(screen_picture, (0, 0))
        for i in range(zivoti):
            screen.blit(scaled_image, (50 * i, 0))
        for y in path:
            pygame.draw.rect(screen, path_color, y)
        for x in popunjene_kucice:
            screen.blit(kucica_puna, (x, 2 * zaba.duzina - 50))
        for y in kucice:
            screen.blit(kucica_prazna, (y, 2 * zaba.duzina - 50))

        #trenutne prepreke
        svi_objekti = []
        dt = clock.tick()

        #pomeranje i iscrtavanje prepreka
        for staza in dinos:
            for prepreka in staza:
                prepreka.update(dt)
                if prepreka.brzina > 0:
                    if prepreka.x_pozicija > screen_width:
                        prepreka.x_pozicija = -prepreka.sirina
                else:
                    if prepreka.x_pozicija < -prepreka.sirina:
                        prepreka.x_pozicija = screen_width + prepreka.sirina
                svi_objekti = [prepreka.draw(screen)] + svi_objekti

        #trenutno pritisnuti tasteri
        keys = pygame.key.get_pressed()
        #promenljiva koja sluzi da se proveri da li se zaba sudarila sa preprekom
        za_koliziju = zaba.draw(screen)
        
        #proverava da li je proslo odredjeno vreme izmedju poteza
        if vreme <= 0:
            running = zaba.update(keys, screen, screen_color, svi_objekti, pomeraj_x, pomeraj_y, za_koliziju)
            vreme = max_vreme
        else:
            vreme -= 1

        #da li je izgubljen zivot
        if not running:
            zivoti -= 1
            return zivoti, zaba_counti, kucice, popunjene_kucice
        
        #provera da li je igrac doveo zabu do odgovarajuce pozicije
        if zaba.y_pozicija < 80:
            prolaz = True
            #zamena nepopunjene i popunjene kucice
            for x in kucice:
                if zaba.x_pozicija in list(range(x, x + 80)) or (zaba.x_pozicija + zaba.sirina) in list(range(x, x + 80)):
                    zaba_counti += 1
                    popunjene_kucice.append(x)
                    kucice.remove(x)
                    prolaz = False
                    return zivoti, zaba_counti, kucice, popunjene_kucice
            #dovedeno na pofresno mesto
            if prolaz:
                zivoti -= 1
                return zivoti, zaba_counti, kucice, popunjene_kucice
        
        pygame.display.flip()
