import pygame
import random

pygame.init()

window_sirina, window_visina = 392, 602
window = pygame.display.set_mode((window_sirina, window_visina))
pygame.display.set_caption("PFETRIS")

bela = (220, 220, 220)
P = (0, 153, 153)
PP = (2, 157, 173)
PPP = (87, 183, 174)
PE= (102, 204, 153)
PEP = (146, 246, 195)
PPE = (83, 229, 166)
PPEP = (188, 4, 90)
PPEPP = (137, 219, 173)
PEE = (123, 312, 144)

# oblici
OBLICI = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 0], [1, 1]]
    
], [
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
    [[1, 0,], [ 1, 1], [0,1]],
    [[1, 0,], [ 1, 1], [1, 0]],
    [[1, 1],[0, 1], [0, 1]],
    [[1, 1], [1, 0]]
   
], [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1], [0, 1]]

], [ 
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
    [[0, 1,], [ 1, 1], [1,0]],
    [[0, 1,], [ 1, 1], [0, 1]],
    [[1, 1],[1, 0],[1, 0]],
    [[0, 1], [1, 1]]
]



#stanja rotacije
stanje = 1

oblik_boje = [P, PP, PPP, PE, PEP, PPE, PPEPP]


kockica_velicina = 30
grid_sirina, grid_visina = window_sirina // kockica_velicina, window_visina // kockica_velicina

grid = [[bela] * grid_sirina for _ in range(grid_visina)]


def draw_grid():
    for red in range(grid_visina):
        for kol in range(grid_sirina):
            pygame.draw.rect(window, grid[red][kol], (kol * kockica_velicina, red * kockica_velicina, kockica_velicina, kockica_velicina))



def draw_blok(blok, pos):
    for red in range(len(blok)):
        for kol in range(len(blok[red])):
            if blok[red][kol]:
                pygame.draw.rect(window, oblik_boje[trenutni_oblik_index], (
                    (pos[0] + kol) * kockica_velicina, (pos[1] + red) * kockica_velicina, kockica_velicina, kockica_velicina))
# pos = [x, y]

def check_kollision(blok, pos):
    for red in range(len(blok)):
        for kol in range(len(blok[red])):
            if blok[red][kol] and (pos[1] + red >= grid_visina or pos[0] + kol < 0 or pos[0] + kol >= grid_sirina
                                        or grid[pos[1] + red][pos[0] + kol] != bela):
                return True
    return False


def obrisi_popunjene_redove():
    popunjene_redove = []
    for red in range(grid_visina):
        if all(kockica != bela for kockica in grid[red]):
            popunjene_redove.append(red) 
    for red in popunjene_redove:
        del grid[red]
        grid.insert(0, [bela] * grid_sirina)

def draw_lines(screen):
    for i in range(grid_sirina+1):
        for j in range(grid_visina+1):
            pygame.draw.line(screen, (199, 199, 199), (i*kockica_velicina, j*kockica_velicina), (i*kockica_velicina, grid_visina*kockica_velicina))
            pygame.draw.line(screen, (199, 199, 199), (i, j*kockica_velicina), (grid_sirina*kockica_velicina, j*kockica_velicina))


trenutni_oblik_index = random.randint(0, len(OBLICI[stanje]) - 1)
trenutni_oblik = OBLICI[stanje][trenutni_oblik_index]
trenutna_pozicija = [grid_sirina // 2 - len(trenutni_oblik[0]) // 2, 0] # [x, y]

clock = pygame.time.Clock()

image_path = "./pfeee.png"
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (50,50))  

game_over = False

# loooop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                if not check_kollision(trenutni_oblik, trenutna_pozicija):
                    trenutna_pozicija[0] -= 1

            elif event.key == pygame.K_RIGHT:
                
                if not check_kollision(trenutni_oblik, trenutna_pozicija):
                    trenutna_pozicija[0] += 1

            elif event.key == pygame.K_DOWN:
                if not check_kollision(trenutni_oblik, trenutna_pozicija):
                    trenutna_pozicija[1] += 1

            elif event.key == pygame.K_UP:
                if not check_kollision(trenutni_oblik, trenutna_pozicija):
                    stanje = (stanje+1) % 4
                    trenutni_oblik = OBLICI[stanje][trenutni_oblik_index]

    trenutna_pozicija[1] += 1

    if check_kollision(trenutni_oblik, trenutna_pozicija):
        trenutna_pozicija[1] -= 1
        for red in range(len(trenutni_oblik)):
            for kol in range(len(trenutni_oblik[red])):
                if trenutni_oblik[red][kol]:
                    grid[trenutna_pozicija[1] + red][trenutna_pozicija[0] + kol] = oblik_boje[trenutni_oblik_index] 

        obrisi_popunjene_redove()

        
        trenutni_oblik_index = random.randint(0, len(OBLICI[stanje]) - 1)
        trenutni_oblik = OBLICI[stanje][trenutni_oblik_index]
        trenutna_pozicija = [grid_sirina // 2 - len(trenutni_oblik[0]) // 2, 0]

        if check_kollision(trenutni_oblik, trenutna_pozicija):
            game_over = True
            print("UMRO SI, VRATI SE KUCI")

    
    window.fill(bela)

    
    draw_grid()
    draw_blok(trenutni_oblik, trenutna_pozicija)
    draw_lines(window)
    window.blit(image, (window_sirina - 55, 7))

    
    pygame.display.update()
    pygame.display.flip()
    
    clock.tick(5)


pygame.quit()
