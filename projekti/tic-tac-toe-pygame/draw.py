import pygame
import random
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
pozadina=(53, 55, 82)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
size=150
indexi=[[[250,70],[570,70],[890,70]],[[250,270],[570,270],[890,270]],[[250,500],[570,500],[890,500]]]
class Iks:
    def __init__(self, _x, _y,xoro):
        self.x = _x
        self.y= _y
        self.xo=xoro
    def draw(self):
        if(self.xo=='X'):
            for i in range(8):
                pygame.draw.aaline(screen,(200,200,200),(self.x+i,self.y),(size+self.x+i,size+self.y))  # start_pos(x+thickness,y)---end_pos(width+x+thickness,height+y)
                pygame.draw.aaline(screen,(200,200,200),(size+self.x+i,self.y),(self.x+i,size+self.y))  
        else:
            pygame.draw.circle(screen, 'black', (self.x+80,self.y+80), 85)
            pygame.draw.circle(screen, pozadina, (self.x+80,self.y+80), 70)
    def provera(self):
        return(self.xo)
class Bot:
    def __init__(self,xo):
        self.xo=xo
    def igra(self,kvadranti):
        popunjen=0
        prazan=0
        kop=[-1,-1]
        # if(kvadranti[1][1]!='' and kvadranti[]): 
        for i in range(3):
            for j in range(3):
                if(kvadranti[i][j]!=''): 
                    if(Iks.provera(kvadranti[i][j])==self.xo):
                        popunjen+=1
                elif(kvadranti[i][j]==''):
                    prazan+=1
                    kop[0]=i
                    kop[1]=j
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            for j in range(3):
                if(kvadranti[j][i]!=''): 
                    if(Iks.provera(kvadranti[j][i])==self.xo):
                        popunjen+=1
                elif(kvadranti[j][i]==''):
                    prazan+=1
                    kop[0]=j
                    kop[1]=i
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            if(kvadranti[i][i]!=''): 
                if(Iks.provera(kvadranti[i][i])==self.xo):
                    popunjen+=1
            elif(kvadranti[i][i]==''):
                prazan+=1
                kop[0]=i
                kop[1]=i
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            if(kvadranti[i][2-i]!=''): 
                if(Iks.provera(kvadranti[i][2-i])==self.xo):
                    popunjen+=1
            elif(kvadranti[i][2-i]==''):
                prazan+=1
                kop[0]=i
                kop[1]=2-i
            # print("pop",popunjen,'pra',prazan)
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
        popunjen=0
        for x in kvadranti:
            for y in x:
                if(y!=''):
                    popunjen+=1
                    
        if(popunjen==1):
            if(kvadranti[1][1]!=''):
                kvadranti[0][0]=Iks(indexi[0][0][0],indexi[0][0][1],self.xo)
                return
            else:
                kvadranti[1][1]=Iks(indexi[1][1][0],indexi[1][1][1],self.xo)
                return
        popunjen=0
        prazan=0
        kop=[-1,-1]
        for i in range(3):
            for j in range(3):
                if(kvadranti[i][j]!=''): 
                    if(Iks.provera(kvadranti[i][j])!=self.xo):
                        popunjen+=1
                elif(kvadranti[i][j]==''):
                    prazan+=1
                    kop[0]=i
                    kop[1]=j
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            for j in range(3):
                if(kvadranti[j][i]!=''): 
                    if(Iks.provera(kvadranti[j][i])!=self.xo):
                        popunjen+=1
                elif(kvadranti[j][i]==''):
                    prazan+=1
                    kop[0]=j
                    kop[1]=i
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            if(kvadranti[i][i]!=''): 
                if(Iks.provera(kvadranti[i][i])!=self.xo):
                    popunjen+=1
            elif(kvadranti[i][i]==''):
                prazan+=1
                kop[0]=i
                kop[1]=i
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
            popunjen=0
            prazan=0
        for i in range(3):
            if(kvadranti[i][2-i]!=''): 
                if(Iks.provera(kvadranti[i][2-i])!=self.xo):
                    popunjen+=1
            elif(kvadranti[i][2-i]==''):
                prazan+=1
                kop[0]=i
                kop[1]=2-i
            # print("pop",popunjen,'pra',prazan)
            if(popunjen==2 and prazan==1):
                kvadranti[kop[0]][kop[1]]=Iks(indexi[kop[0]][kop[1]][0],indexi[kop[0]][kop[1]][1],self.xo)
                return
        if(kvadranti[0][2]!='' and kvadranti[1][1]!='' and kvadranti[2][0]!='' and kvadranti[0][1]==''):
            if(Iks.provera(kvadranti[0][2])!=self.xo and Iks.provera(kvadranti[1][1])==self.xo and Iks.provera(kvadranti[2][0])!=self.xo):
                kvadranti[0][1]=Iks(indexi[0][1][0],indexi[0][1][1],self.xo)
                return
        if(kvadranti[0][0]!='' and kvadranti[1][1]!='' and kvadranti[2][2]!='' and kvadranti[0][2]==''):
            if(Iks.provera(kvadranti[0][0])==self.xo and Iks.provera(kvadranti[1][1])!=self.xo and Iks.provera(kvadranti[2][2])!=self.xo):
                kvadranti[0][2]=Iks(indexi[0][2][0],indexi[0][2][1],self.xo)
                return
        for i in range(3):
            for j in range(3):
                if(kvadranti[i][j]==''):
                    kvadranti[i][j]=Iks(indexi[i][j][0],indexi[i][j][1],self.xo)
                    return
            






        

        






















