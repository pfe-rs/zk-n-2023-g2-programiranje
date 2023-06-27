
import random
import pygame
pygame.init()

def random_rec():
    with open('wordle 5 letter words2.txt') as f:
        reci = f.read().splitlines()
        return random.choice(reci)
    
rec = random_rec()
#print(rec)
belo = (128, 0, 128) #ljubcasto
real_belo = (255, 255, 255)
crno = (242, 210, 189) #pozadina
green = (0, 255, 0) 
zuto = (255, 255, 51)
sivo = (128, 0, 128) #ljub
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
promena = 0
tabla = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
 
fps = 60
sat = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 56)
winner_font = pygame.font.Font('freesansbold.ttf', 100)
trazeno = pygame.font.Font('freesansbold.ttf', 25)

zadata_rec = rec
kraj = False
slova = 0
trenutno = True
def crtanje_table():
    global promena
    global tabla

    for kolona in range(0, 5):
        for red in range(0, 6):
            pygame.draw.rect(screen, belo, [kolona * 100 + 12, red * 100 + 12, 75, 75], 3, 5)
            slovo = font.render(tabla[red][kolona], True, sivo)
            screen.blit(slovo, (kolona * 100 + 30, red * 100 + 25))

def provera_slova():
    global promena
    global tabla
    global zadata_rec
    
    
    nalazi_zel = []
    nalazi_zut = []

    for kolona in range(0, 5):
        for red in range(0, 6):
            if  zadata_rec[kolona] == tabla[red][kolona] and promena > red:
                if kolona not in nalazi_zel:  
                    nalazi_zel.append(kolona)
                pygame.draw.rect(screen, (green), [kolona * 100 + 12, red * 100 + 12, 75, 75], 0, 5)
            elif tabla[red][kolona] != zadata_rec[kolona] and tabla[red].count(tabla[red][kolona]) <= zadata_rec.count(tabla[red][kolona]) and promena > red:
                nalazi_zut.append(kolona)
                pygame.draw.rect(screen, zuto, [kolona * 100 + 12, red * 100 + 12, 75, 75], 0, 5)
            last_row_guess = tabla[5][0] + tabla[5][1] + tabla[5][2] + tabla[5][3] + tabla[5][4]
            if last_row_guess == zadata_rec and promena == 6 :
                kraj = True

                for kolona in range(0, 5):
                    if  zadata_rec[kolona] == tabla[red][kolona] and promena > red:
                        if kolona not in nalazi_zel:  
                            nalazi_zel.append(kolona)
                        pygame.draw.rect(screen, (green), [kolona * 100 + 12, red * 100 + 12, 75, 75], 0, 5)
                    elif tabla[red][kolona] != zadata_rec[kolona] and tabla[red].count(tabla[red][kolona]) <= zadata_rec.count(tabla[red][kolona]) and promena > red:
                        nalazi_zut.append(kolona)
                        pygame.draw.rect(screen, zuto, [kolona * 100 + 12, red * 100 + 12, 75, 75], 0, 5) 


running = True
while running:
    sat.tick(fps)
    screen.fill(crno)
    provera_slova()
    crtanje_table()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.TEXTINPUT and trenutno and not kraj:
                ulaz = event.__getattribute__('text')
                if ulaz != " ":
                    ulaz = ulaz.lower()
                    tabla[promena][slova] = ulaz
                    slova += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and slova > 0:
                tabla[promena][slova - 1] = ' '
                slova -= 1
            if event.key == pygame.K_SPACE and not kraj:
                if slova < 5:
                    nedovoljno_slova = 'you didnt enter enough letters'
                    nedovoljno_slova = trazeno.render(nedovoljno_slova, True, belo)
                    screen.blit(nedovoljno_slova, (20, 600))
                    pygame.display.update()
                    pygame.time.delay(2000)

                if slova == 5:
                    promena += 1
                    slova = 0
            if event.key == pygame.K_SPACE and kraj:
                promena = 0
                slova = 0
                kraj = False
                tabla = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

        
                
        if slova == 5:
            trenutno = False
        if slova < 5:
            trenutno = True

        for red in range(0 , 6):
            guess = tabla[red][0] + tabla[red][1] + tabla[red][2] + tabla[red][3] + tabla[red][4]
            if guess == zadata_rec and red < promena:
                kraj = True
                
        if promena == 6 and kraj == False:

            kraj = True
            ispis = 'Loser!'
            trazena_rec = 'the word was: ' + rec

            rect_width = 300
            rect_height = 100
            rect_x = (SCREEN_WIDTH - rect_width) // 2
            rect_y = (SCREEN_HEIGHT - rect_height) // 2
            pygame.draw.rect(screen, belo, (rect_x, rect_y, rect_width, rect_height))

            ispis = winner_font.render(ispis, True, real_belo)
            trazena_rec = trazeno.render(trazena_rec, True, belo) 
            screen.blit(ispis, (SCREEN_WIDTH / 2 - ispis.get_width() / 2, SCREEN_HEIGHT / 2 - ispis.get_height() / 2))
            screen.blit(trazena_rec, (20, 600))
            pygame.display.update()
            pygame.time.delay(2000)
            promena = 7
            running = False


            
        elif kraj and promena <= 6:

            ispis = 'Winner!'
            rect_width = 400
            rect_height = 100
            rect_x = (SCREEN_WIDTH - rect_width) // 2
            rect_y = (SCREEN_HEIGHT - rect_height) // 2
            pygame.draw.rect(screen, belo, (rect_x, rect_y, rect_width, rect_height))

            ispis = winner_font.render(ispis, True, real_belo)
            screen.blit(ispis, (SCREEN_WIDTH / 2 - ispis.get_width() / 2, SCREEN_HEIGHT / 2 - ispis.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False

    pygame.display.flip()
    
pygame.quit()