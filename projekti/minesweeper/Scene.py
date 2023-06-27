import pygame
import random
import numpy as np
from pygame.locals import *


class Button:
    def __init__(self, x, y, width, height, inactive_color, active_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.active_color, self.rect)
        else:
            pygame.draw.rect(screen, self.inactive_color, self.rect)


class SveScene():

   # import pygame
   #import numpy as np
    #import random
    # Example file showing a basic pygame "game loop"

    # pygame setup
    def __init__(self):
        self.image_path = "slika.png"
        self.image = pygame.image.load(self.image_path)


        self.image_path1 = "zastavica.png"
        self.zastava = pygame.image.load(self.image_path1)

        self.image_path2 = "gameover.jpg"
        self.gmvr = pygame.image.load(self.image_path2)

        self.image_path2 = "pobeda.jpeg"
        self.pobeda = pygame.image.load(self.image_path2)




        self.number_of_tiles = 10

        self.sW = 720
        self.sH = 720
        self.distance = int(self.sW / self.number_of_tiles)
        self.zastava = pygame.transform.scale(self.zastava, (self.distance, self.distance))
        self.gmvr = pygame.transform.scale(self.gmvr, (720, 720))

        pygame.init()
        self.broj_mina = 0
        self.sW = 720
        self.sH = 720
        self.screen = pygame.display.set_mode((self.sW, self.sH))
        self.clock = pygame.time.Clock()
        self.running = True
        self.number_of_tiles = 10

        self.distance = int(self.sW / self.number_of_tiles)

        #pod = pygame.Rect(0, 500, 1500, 1500)
        #tank = pygame.Rect(50, 500, 50, 50)


        self.matrica = np.zeros((self.number_of_tiles, self.number_of_tiles))
        self.matrica1 = np.zeros((self.number_of_tiles, self.number_of_tiles))
        self.matrica_zastava = np.zeros((self.number_of_tiles, self.number_of_tiles))

        prob_of_bomb = 0.1

        for i in range(self.number_of_tiles):
            for k in range(self.number_of_tiles):
                g = random.random()
                if g > 1 - prob_of_bomb:
                    self.matrica[i, k] = 1  

        self.a = np.zeros((self.matrica.shape))

        for i in range(self.a.shape[0]):
            for j in range(self.matrica.shape[1]):
                for f in range(-1, 2):
                    for k in range(-1, 2):
                        if i + f > -1 and i + f < self.a.shape[0]  and j + k > -1 and j + k < self.a.shape[1]:
                            self.a[i, j] += self.matrica[i + f, j + k]
        self.x = 50
        #self.boolean = False
        #zelena = False
        self.lista = []
        self.lista1 = []
        self.lista2 = []
    def PocetniEkran(self):
        self.screen.fill((1, 1, 230))
        self.screen.blit(self.image, (100, 100))
        pygame.display.flip()
        pygame.display.update()
    def UI(self):



        text  = "TESKO"
        input_box = pygame.Rect(530, 250, 140, 30)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        font = pygame.font.Font(None, 32)
        
        text1  = "LAKO"
        input_box1 = pygame.Rect(50, 250, 140, 30)
        color_inactive1 = pygame.Color('lightskyblue3')
        color_active1 = pygame.Color('dodgerblue2')
        color1 = color_inactive
        font1 = pygame.font.Font(None, 32)

        text2  = "SREDNJE"
        input_box2 = pygame.Rect(290, 250, 140, 30)
        color_inactive2 = pygame.Color('lightskyblue3')
        color_active2 = pygame.Color('dodgerblue2')
        color2 = color_inactive
        font2 = pygame.font.Font(None, 32)


        active = True





        while active:

            for event in pygame.event.get():
            #   if event.type == QUIT:
            #      done = True
                if pygame.mouse.get_pressed()[0]: 
                    try:
                        pos = pygame.mouse.get_pos()
                        x1, y1 = pos
                        print(x1, y1)
                        print(input_box.x)
                        print(input_box.x + 50)

                        print(input_box.y)
                        print(input_box.y + 50)
                        if x1 > input_box.x and x1 < input_box.x + 200 and y1 > input_box.y and input_box.y + 30 > y1:
                            self.broj_gresaka = 1
                            active = False 

                        if x1 > input_box1.x and x1 < input_box1.x + 200 and y1 > input_box1.y and input_box1.y + 30 > y1:
                            self.broj_gresaka = 3
                            active = False


                        if x1 > input_box2.x and x1 < input_box2.x + 200 and y1 > input_box2.y and input_box2.y + 30 > y1:
                            self.broj_gresaka = 2
                            active = False




                    except KeyboardInterrupt:
                        break
                self.screen.fill((0, 0, 255))
                pygame.draw.rect(self.screen, color, input_box, 2)
                pygame.draw.rect(self.screen, color, input_box1, 2)
                pygame.draw.rect(self.screen, color, input_box2, 2)

                text_surface = font.render(text, True, (0, 0, 0))
                text_surface1 = font.render(text1, True, (0, 0, 0))
                text_surface2 = font.render(text2, True, (0, 0, 0))

                self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
                self.screen.blit(text_surface1, (input_box1.x + 5, input_box1.y + 5))
                self.screen.blit(text_surface2, (input_box2.x + 5, input_box2.y + 5))


                pygame.display.flip()







    def ProveraZavrsen(self):
        if self.broj_mina == self.broj_gresaka:
            return False
        else:
            return True

    def ProveraPobede(self):
        if np.sum(abs(self.matrica - self.matrica_zastava)) == 0:
            return False
        else:
            return True
    def Glavna(self):
        
            #tank = pygame.Rect(self.x, 500, 50, 50)
        self.screen.fill((1, 100, 1))
        # poll for events})>
        # pygame.QUIT event means the})> user clicked X to close your window
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
    
                self.running = False
        

        for i in range(self.number_of_tiles + 1):
            pygame.draw.line(self.screen, "black", (i * self.distance, 0), (i * self.distance, self.sH), 5)
    
        for k in range(self.number_of_tiles + 1):
            pygame.draw.line(self.screen, "black", (0, k * self.distance), (self.sW, k * self.distance), 5)
        #if boolean:
    
    
        for x in range(self.number_of_tiles):
            for y in range(self.number_of_tiles):
                #print(np.max(self.matrica_zastava))
                if self.matrica_zastava[x, y] != 0.0:
                    print(self.matrica_zastava[x, y])
                    print(x, y)
                    if not((x, y) in self.lista2):
                        self.screen.blit(self.zastava, (x* self.distance, y * self.distance))
                        #pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(x * self.distance, y * self.distance, self.distance, self.distance))
                    #print("aaa")

                if self.matrica1[x,y] == 1:
                    if not((x, y) in self.lista):
                        self.lista.append((x,y))
                    #self.broj_mina += 1
                    #pygame.draw.rect(self.screen, "red", pygame.Rect(x1 * self.distance, y1 * self.distance, self.distance, self.distance))

                
                elif self.matrica1[x,y] == -1:
                    if not((x, y) in self.lista1):
                        self.lista1.append((x, y))
                   # pygame.draw.rect(self.screen, "blue", pygame.Rect(x1 * self.distance, y1 * self.distance, self.distance, self.distance))
    
        
        for kor in self.lista:
            x1, y1 = kor
            pygame.draw.rect(self.screen, "red", pygame.Rect(x1 * self.distance, y1 * self.distance, self.distance, self.distance))
    
    
    

    
        for kor in self.lista1:
            broj = 0
            x1, y1 = kor
    
            #for i in range(-1, 1):
            #   for k in range(-1, 1):
            #      broj += self.matrica[max(min(x1 + i,self.number_of_tiles-1), 0), max(min(y1 + k, self.number_of_tiles-1), 0)] 
            broj = self.a[x1, y1]
            pygame.draw.rect(self.screen, (0, 0, int(255 / 8 * broj)), pygame.Rect(x1 * self.distance, y1 * self.distance, self.distance, self.distance))
        
        for kor in self.lista2:
            x1, y1 = kor

            pass
    # for k in range(self.number_of_tiles):
    
    
            
        # RENDER YOUR GAME HERE
    
        # flip() the display to put your work on self.screen
        #pygame.draw.rect(self.screen, (100, 100, 0), pod)
        #pygame.draw.rect(self.screen, (0, 100, 0), tank)
    
    
        
        pygame.display.flip()
        x, y = pygame.mouse.get_pos()
    
        self.clock.tick(60)  # limits FPS to 60
    
    
        ev = pygame.event.get()

        #self.n_otkacenih = np.equals((self.matrica1, 0))

        #self.sum_n_otkacenih = np.sum(self.n_otkacenih)
        
        #if self.sum_n_otkacenih == 2:
        #    pass
    
        # proceed events
        for event in ev:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[2]: 
                    #try:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    kliknuto_polje = np.ceil(pos[0] / self.distance), np.ceil(pos[1] / self.distance)
                    x1= int(kliknuto_polje[0]) -  1
                    y1 = int(kliknuto_polje[1])  - 1

                    # boolean = True
                    self.matrica_zastava[x1, y1] = not(self.matrica_zastava[x1, y1])
                    print(x1, y1)

                    #except KeyboardInterrupt:
                      #  print("interrupt")
            


            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: 
                    try:
                        pos = pygame.mouse.get_pos()
                        print(pos)
                        kliknuto_polje = np.ceil(pos[0] / self.distance), np.ceil(pos[1] / self.distance)
                        x1= int(kliknuto_polje[0]) -  1
                        y1 = int(kliknuto_polje[1])  - 1
                        print(x1, y1)
                        if self.matrica[x1, y1] == 1:
        
                            
                        # boolean = True
                            self.broj_mina += 1
                            self.matrica1[x1, y1] = 1
                        else:
                            #zelena = True
                            self.matrica1[x1, y1] = -1
                    except KeyboardInterrupt:
                        print("interrupt")


            # get a list of all sprites that are under the mouse cursor
            #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
    def ZavrsniEkran(self):


        self.screen.fill((1, 1, 230))
        self.screen.blit(self.gmvr, (0, 0))
        pygame.display.flip()
        pygame.display.update()

    def Pobeda(self):


        self.screen.fill((1, 1, 230))
        self.screen.blit(self.pobeda, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        #pygame.display.flip()