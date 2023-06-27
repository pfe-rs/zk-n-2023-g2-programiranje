import pygame

screen_height = 720
screen_width = 1280

svi_objekti = []


class Caracter:
    def __init__(self, x_pozicija=200, y_pozicija=200, x_dimenzija=100, y_dimenzija=100, boja=(0, 0, 0)):
        self.boja = boja
        self.sirina = x_dimenzija
        self.duzina = y_dimenzija
        self.x_pozicija = x_pozicija
        self.y_pozicija = y_pozicija

    #crtanje objekta
    def draw(self, screen):
        rect = pygame.Rect(self.x_pozicija, self.y_pozicija, self.sirina, self.duzina)
        pygame.draw.rect(screen, self.boja, rect)
        return rect
    

class Frog(Caracter):
    def __init__(self, x_pozicija, y_pozicija, x_dimenzija, y_dimenzija, boja):
        super().__init__(x_pozicija, y_pozicija, x_dimenzija, y_dimenzija, boja)
    
    #pomeranje zabe i pozivanje funkcije za crtanje
    def update(self, keys, screen, screen_color, svi_objekti, pomeraj_x, pomeraj_y, zaba):
        deo = 3
        #levo
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            for i in range(pomeraj_x // deo):
                if self.proveri(svi_objekti, zaba):
                    if self.x_pozicija >= deo:
                        screen.fill(screen_color)
                        self.x_pozicija -= deo
                        self.draw(screen)
                    else:
                        break
                else:
                    return False
            return True
        
        #desno
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            for i in range(pomeraj_x):
                if self.proveri(svi_objekti, zaba):
                    if self.x_pozicija < screen_width - self.sirina:
                        screen.fill(screen_color)
                        self.x_pozicija += 1
                        self.draw(screen)
                    else:
                        break
                else:
                    return False
            return True

        #gore
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            for i in range(pomeraj_y):
                if self.proveri(svi_objekti, zaba):
                    if self.y_pozicija > 1:
                        screen.fill(screen_color)
                        self.y_pozicija -= 1
                        self.draw(screen)
                    else:
                        break
                else:
                    return False
            return True

        #dole
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            for i in range(pomeraj_y):
                if self.proveri(svi_objekti, zaba):
                    if self.y_pozicija < screen_height - self.duzina:
                        screen.fill(screen_color)
                        self.y_pozicija += 1
                        self.draw(screen)
                    else:
                        break
                else:
                    return False
            return True
        
        #ostaje u mestu
        else:
            if not self.proveri(svi_objekti, zaba):
                return False
            return True
        

    #provera da li se objekat sudara sa ostalim
    def proveri(self, svi_objekti, zaba):
        running = True
        for i in svi_objekti:
            if i.colliderect(zaba):
                running = False
                return running 
        return running   


class Prepreka(Caracter):
    
    def __init__(self, x_pozicija, y_pozicija, brzina, x_dimenzija, y_dimenzija, boja):
        super().__init__(x_pozicija, y_pozicija, x_dimenzija, y_dimenzija, boja)
        self.brzina = brzina

    #pomeranje objekata
    def update(self, dt):
        self.x_pozicija += self.brzina * dt / 1000
