import pygame
import math
import pygame.time


pygame.init()


sirina_prozora = 800
visina_prozora = 600
prozor = pygame.display.set_mode((sirina_prozora, visina_prozora))
pygame.display.set_caption("Angry Birds")


ROZE = (180, 0, 50)
CRNA = (0, 0, 0)
BELA = (255, 255, 255)
ZELENA=(0,180,0)
ZELENA_2=(0,80,0)
NEBO=(50,200,200)
BRAON=(80,50,10)
TAMNO_ZELENA=(0,120,0)


loptica_x = 100
loptica_y = visina_prozora - 100
loptica_radius = 20
loptica_nategnuta = False
loptica_napetost = 0



pracka_x = 150
pracka_y = visina_prozora - 150
pracka_duzina = 100
pracka_debljina = 15
loptica_ispaljena = False


abcd_x=loptica_x-14.1
abcd_y=loptica_y-14.1
abcd=pygame.Rect(abcd_x, abcd_y, 28.2, 28.2)


pod=pygame.Rect(0,visina_prozora-150, sirina_prozora, 150)
daska_1=pygame.Rect(500, visina_prozora-250, 20, 100)
daska_2=pygame.Rect(620, visina_prozora-250, 20, 100)
daska_3=pygame.Rect(470, visina_prozora-270, 200, 20)


pig_radius = 25
pig_x=570
pig_y=visina_prozora-295


rec_x=pig_x-17.625
rec_y=pig_y-17.625
rec = pygame.Rect(rec_x, rec_y, 35.25, 35.25)


eye1_x=rec_x+10.5
eye1_y=rec_y+10.5
eye2_x=rec_x+24.3
eye2_y=rec_y+10.5


ear1_x=rec_x+3
ear1_y=rec_y-3
ear2_x=rec_x+31.5
ear2_y=rec_y-3


start_time=0
p=0
i=0
k=0
l=0


pf=False
sf=False


dx=0
dy=0


running = True
while running:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not loptica_nategnuta:
                loptica_nategnuta = True
                loptica_ispaljena = False
                sf=True
                pf=False


        elif event.type == pygame.MOUSEBUTTONUP:
            if loptica_nategnuta:
                loptica_nategnuta = False
                loptica_ispaljena = True
                sf=False
                pf=True


    if(sf==True and pf==False):
       p=0


    if(sf==False and pf==True):
       p +=1
    
    if(p==1):
       start_time=pygame.time.get_ticks()


    if loptica_nategnuta:            
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = pracka_x-loptica_x
        dy = loptica_y-pracka_y


        loptica_x, loptica_y = mouse_x, mouse_y
        abcd_x, abcd_y = loptica_x - 14.1, loptica_y - 14.1


        loptica_napetost = math.sqrt(dx ** 2 + dy ** 2)
       
    
        


    prozor.fill(NEBO)
    pygame.draw.rect(prozor, ZELENA, pod)
    pygame.draw.rect(prozor, BRAON, daska_1)
    pygame.draw.rect(prozor, BRAON, daska_2)
    pygame.draw.rect(prozor, BRAON, daska_3)
    pygame.draw.circle(prozor, ZELENA_2, (ear1_x, ear1_y), 9)
    pygame.draw.circle(prozor, ZELENA_2, (ear2_x, ear2_y), 9)
    pygame.draw.circle(prozor, TAMNO_ZELENA, (pig_x, pig_y), pig_radius)
    pygame.draw.circle(prozor, CRNA, (eye1_x, eye1_y), 2.75)
    pygame.draw.circle(prozor, CRNA, (eye2_x, eye2_y), 2.75)
    
    
    if not loptica_ispaljena:
        pygame.draw.line(prozor, CRNA, (pracka_x, pracka_y), (loptica_x, loptica_y), pracka_debljina)
        
    
    if loptica_nategnuta:
       pygame.draw.circle(prozor, ROZE, (loptica_x, loptica_y), loptica_radius)
    else:
       pygame.draw.circle(prozor, CRNA, (loptica_x, loptica_y), loptica_radius)


   
    
   
   
    if loptica_ispaljena :
     
        elapsed_time=pygame.time.get_ticks()-start_time
    
        speed_x = dx/ 64
        speed_y = dy/64 - 0.002*elapsed_time
     
        
        loptica_y -= speed_y
        loptica_x += speed_x
        abcd_y -= speed_y
        abcd_x += speed_x


    abcd = pygame.Rect(abcd_x, abcd_y, 28.2, 28.2)
    rec = pygame.Rect(rec_x, rec_y, 35.25, 35.25)
    
    rec_x=pig_x-17.625
    rec_y=pig_y-17.625


    eye1_x=rec_x+10.5
    eye1_y=rec_y+10.5
    eye2_x=rec_x+24.3
    eye2_y=rec_y+10.5


    ear1_x=rec_x+3
    ear1_y=rec_y-3
    ear2_x=rec_x+31.5
    ear2_y=rec_y-3


    if abcd.colliderect(rec):
        i=1
        k+=1
        
    if(k==1):
        start_time2=pygame.time.get_ticks()
    
    if(i==1):  
        elapsed_time2=pygame.time.get_ticks()-start_time2 
        pig_x+=(speed_x/2)*3
        pig_y-=speed_y/2- 0.002*elapsed_time2


    
    
    pygame.display.flip()


pygame.quit()

