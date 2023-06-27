import pygame
from draw import Iks
from draw import Bot
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
pozadina=(53, 55, 82)
horizontalna = pygame.Rect(200, 240 , 880, 10)
horizontalna2 = pygame.Rect(200, 480, 880, 10)
vertikalna = pygame.Rect(456, 50 , 10, 600)
vertikalna2 = pygame.Rect(822, 50 , 10, 600)
kvadranti=[['','',''],['','',''],['','','']]
indexi=[[[250,70],[570,70],[890,70]],[[250,270],[570,270],[890,270]],[[250,500],[570,500],[890,500]]]
red=0
igra=-1
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Igra je neresena', True, 'black', pozadina)
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT // 2)
text2 = font.render('Vrati se na pocetnu', True, 'black', 'white')
textRect2 = text2.get_rect()
textRect2.center = (SCREEN_WIDTH//2, (SCREEN_HEIGHT // 2 )+ 50)
text3 = font.render('Igraj igrac protiv igraca', True, 'black', 'pink')
text4 = font.render('Igraj protiv bota', True, 'black', 'light green')
textRect3 = text3.get_rect()
textRect3.center = (SCREEN_WIDTH//2, (SCREEN_HEIGHT // 2 ))
textRect4 = text4.get_rect()
textRect4.center = (SCREEN_WIDTH//2, (SCREEN_HEIGHT // 2 )+ 50)
bot=Bot('O')
while running:
    screen.fill(pozadina)
    dt = clock.tick(60)
    if(igra==0 or igra==4):
        pygame.draw.rect(screen, (0,0,0), horizontalna)
        pygame.draw.rect(screen, (0,0,0), horizontalna2)
        pygame.draw.rect(screen, (0,0,0), vertikalna)
        pygame.draw.rect(screen, (0,0,0), vertikalna2)
        if(kvadranti[0][0]!=''):
                Iks.draw(kvadranti[0][0])
        if(kvadranti[1][0]!=''):
                Iks.draw(kvadranti[1][0])
        if(kvadranti[2][0]!=''):
                Iks.draw(kvadranti[2][0])
        if(kvadranti[0][1]!=''):
                Iks.draw(kvadranti[0][1])
        if(kvadranti[1][1]!=''):
                Iks.draw(kvadranti[1][1])
        if(kvadranti[2][1]!=''):
                Iks.draw(kvadranti[2][1])
        if(kvadranti[0][2]!=''):
                Iks.draw(kvadranti[0][2])
        if(kvadranti[1][2]!=''):
                Iks.draw(kvadranti[1][2])
        if(kvadranti[2][2]!=''):
                Iks.draw(kvadranti[2][2])
    #crtanje
    if(igra==-1):
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
    ev = pygame.event.get()
    if(igra!=0 and igra!=-1):
        if(igra==1):
            text = font.render('Igra je neresena', True, 'black', pozadina)
            screen.blit(text, textRect)
            screen.blit(text2, textRect2)
            kvadranti=[['','',''],['','',''],['','','']]
            red=0
        if(igra==2):
            text=font.render('POBEDIO JE X', True, 'black', pozadina)
            screen.blit(text, textRect)
            screen.blit(text2, textRect2)
            kvadranti=[['','',''],['','',''],['','','']]
            red=0
        if(igra==3):
            text=font.render('POBEDIO JE O', True, 'black', pozadina)
            screen.blit(text, textRect)
            screen.blit(text2, textRect2)
            kvadranti=[['','',''],['','',''],['','','']]
            red=0
    #pobeda nereseno itd
    if(igra==4):
        if(red==1):
            red=0
            Bot.igra(bot,kvadranti)

              
    for event in ev:  
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if(igra==0 or igra==4):
                if(red==0):
                    if(pos[0]<456):
                        if(pos[1]<240 and kvadranti[0][0]==''):
                            kvadranti[0][0]=Iks(250,70,'X')  
                            Iks.draw(kvadranti[0][0])
                            red=1
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][0]==''):
                            kvadranti[1][0]=Iks(250,270,'X')  
                            Iks.draw(kvadranti[1][0])
                            red=1
                        elif(pos[1]>480 and kvadranti[2][0]==''):
                            kvadranti[2][0]=Iks(250,500,'X')  
                            Iks.draw(kvadranti[2][0])
                            red=1
                    elif(pos[0]<822):
                        if(pos[1]<240 and kvadranti[0][1]==''):
                            kvadranti[0][1]=Iks(570,70,'X')  
                            Iks.draw(kvadranti[0][1])
                            red=1
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][1]==''):
                            kvadranti[1][1]=Iks(570,270,'X')  
                            Iks.draw(kvadranti[1][1])
                            red=1
                        elif(pos[1]>480 and kvadranti[2][1]==''):
                            kvadranti[2][1]=Iks(570,500,'X')  
                            Iks.draw(kvadranti[2][1])
                            red=1
                    elif(pos[0]>822):
                        if(pos[1]<240 and kvadranti[0][2]==''):
                            kvadranti[0][2]=Iks(890,70,'X')  
                            Iks.draw(kvadranti[0][2])
                            red=1
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][2]==''):
                            kvadranti[1][2]=Iks(890,270,'X')  
                            Iks.draw(kvadranti[1][2])
                            red=1
                        elif(pos[1]>480 and kvadranti[2][2]==''):
                            kvadranti[2][2]=Iks(890,500,'X')  
                            Iks.draw(kvadranti[2][2])
                            red=1
                elif(red==1):
                    if(pos[0]<456):
                        if(pos[1]<240 and kvadranti[0][0]==''):
                            kvadranti[0][0]=Iks(250,70,'O')  
                            Iks.draw(kvadranti[0][0])
                            red=0
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][0]==''):
                            kvadranti[1][0]=Iks(250,270,'O')  
                            Iks.draw(kvadranti[1][0])
                            red=0
                        elif(pos[1]>480 and kvadranti[2][0]==''):
                            kvadranti[2][0]=Iks(250,500,'O')  
                            Iks.draw(kvadranti[2][0])
                            red=0
                    elif(pos[0]<822):
                        if(pos[1]<240 and kvadranti[0][1]==''):
                            kvadranti[0][1]=Iks(570,70,'O')  
                            Iks.draw(kvadranti[0][1])
                            red=0
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][1]==''):
                            kvadranti[1][1]=Iks(570,270,'O')  
                            Iks.draw(kvadranti[1][1])
                            red=0
                        elif(pos[1]>480 and kvadranti[2][1]==''):
                            kvadranti[2][1]=Iks(570,500,'O')  
                            Iks.draw(kvadranti[2][1])
                            red=0
                    elif(pos[0]>822):
                        if(pos[1]<240 and kvadranti[0][2]==''):
                            kvadranti[0][2]=Iks(890,70,'O')  
                            Iks.draw(kvadranti[0][2])
                            red=0
                        elif(pos[1]>240 and pos[1]<480 and kvadranti[1][2]==''):
                            kvadranti[1][2]=Iks(890,270,'O')  
                            Iks.draw(kvadranti[1][2])
                            red=0
                        elif(pos[1]>480 and kvadranti[2][2]==''):
                            kvadranti[2][2]=Iks(890,500,'O')  
                            Iks.draw(kvadranti[2][2])
                            red=0
            if(igra==-1):
                if(pos[0]>SCREEN_WIDTH//2-170 and pos[1]>(SCREEN_HEIGHT // 2 )-20 and pos[0]<SCREEN_WIDTH//2+170 and pos[1]<(SCREEN_HEIGHT // 2 )+20):
                     igra=0
                if(pos[0]>SCREEN_WIDTH//2-170 and pos[1]>(SCREEN_HEIGHT // 2 )+30 and pos[0]<SCREEN_WIDTH//2+170 and pos[1]<(SCREEN_HEIGHT // 2 )+70):
                     igra=4
            if(igra!=0 and igra!=4):
                 if(pos[0]>SCREEN_WIDTH//2-170 and pos[1]>(SCREEN_HEIGHT // 2 )+30 and pos[0]<SCREEN_WIDTH//2+170 and pos[1]<(SCREEN_HEIGHT // 2 )+70):
                     igra=-1
        if event.type == pygame.QUIT:
            running = False 
    for i in range(3):
        if(kvadranti[i][0]!='' and kvadranti[i][1]!='' and kvadranti[i][2]!='' and Iks.provera(kvadranti[i][0])==Iks.provera(kvadranti[i][1])==Iks.provera(kvadranti[i][2])):
            if(Iks.provera(kvadranti[i][0])=='X'): #0 je x, 1 je o
                igra=2
            if(Iks.provera(kvadranti[i][0])=='O'): #0 je x, 1 je o
                igra=3
        if(kvadranti[0][i]!='' and kvadranti[1][i]!='' and kvadranti[2][i]!='' and Iks.provera(kvadranti[0][i])==Iks.provera(kvadranti[1][i])==Iks.provera(kvadranti[2][i])):
            if(Iks.provera(kvadranti[0][i])=='X'): #0 je x, 1 je o
                igra=2
                # print('a')
            if(Iks.provera(kvadranti[0][i])=='O'): #0 je x, 1 je o
                igra=3
                # print('b')
    if(kvadranti[0][0]!='' and kvadranti[1][1]!='' and kvadranti[2][2]!='' and Iks.provera(kvadranti[0][0])==Iks.provera(kvadranti[1][1])==Iks.provera(kvadranti[2][2])):
            if(Iks.provera(kvadranti[1][1])=='X'): #0 je x, 1 je o
                igra=2
                # print('a')
            if(Iks.provera(kvadranti[1][1])=='O'): #0 je x, 1 je o
                igra=3
                # print('b')
    if(kvadranti[0][2]!='' and kvadranti[1][1]!='' and kvadranti[2][0]!='' and Iks.provera(kvadranti[0][2])==Iks.provera(kvadranti[1][1])==Iks.provera(kvadranti[2][0])):
            if(Iks.provera(kvadranti[0][2])=='X'): #0 je x, 1 je o
                igra=2
                # print('a')
            if(Iks.provera(kvadranti[0][2])=='O'): #0 je x, 1 je o
                igra=3
                # print('b')
    provera=0
    for i in range(3):    
        for j in range(3):
            if(kvadranti[i][j]==''):
                break
            provera+=1
        # print(provera)
    if(provera==9): 
        igra=1      
    #upisivanje i provera da li je neko pobedio, quit
    
    pygame.display.flip()
























