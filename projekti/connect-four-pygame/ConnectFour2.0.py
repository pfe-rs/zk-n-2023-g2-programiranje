def proveri(tabela, y, x):
    igrac = tabela[y][x]
    brojac = 0
    dx, dy = 1, 1
    while x - dx >= 0 and y - dy >= 0 and igrac == tabela[y - dy][x - dx]:
        brojac += 1
        dx += 1
        dy += 1
    dx, dy = 1, 1
    while x + dx <= 6 and y + dy <= 6 and igrac == tabela[y + dy][x + dx]:
        brojac += 1
        dx += 1
        dy += 1
    if brojac >= 3:
        return igrac
    brojac, dx, dy = 0, 1, 1

    while x - dx >= 0 and y + dy <= 6 and igrac == tabela[y + dy][x - dx]:
        brojac += 1
        dx += 1
        dy += 1
    dx, dy = 1, 1
    while x + dx <= 6 and y - dy >= 0 and igrac == tabela[y - dy][x + dx]:
        brojac += 1
        dx += 1
        dy += 1
    if brojac >= 3:
        return igrac
    brojac, dx, dy = 0, 1, 1

    while y + dy <= 6 and tabela[y + dy][x] == igrac:
        brojac += 1
        dy += 1
    if brojac >= 3:
        return igrac
    brojac, dy = 0, 1

    while x - dx >= 0 and igrac == tabela[y][x - dx]:
        brojac += 1
        dx += 1
    while x + dx <= 6 and igrac == tabela[y][x + dx]:
        brojac += 1
        dx += 1
    if brojac >= 3:
        return igrac
    return None

import pygame as pd

pd.init()
sirina, visina = 840, 840
ekran = pd.display.set_mode((sirina, visina))
pd.display.set_caption('Connect Four 2.0')

running = True
igrac = True
boja_pozadine = ("black")
popunjeno = [0, 0, 0, 0, 0, 0, 0]
trenutnaPozicija = 0

tabla = []
for i in range(7):
    tabla.append([])
    for j in range(7):
        tabla[i].append(None)

prethodno = True
tabla[0][0] = igrac

while running:
    for event in pd.event.get():
        if event.type == pd.QUIT:
            running = not running
 

    kljucevi = pd.key.get_pressed()

    if kljucevi[pd.K_LEFT]:
        if prethodno:
            if trenutnaPozicija > 0:
                trenutnaPozicija -= 1
                tabla[0][trenutnaPozicija] = igrac
                tabla[0][trenutnaPozicija + 1] = None
        prethodno = False
            
    elif kljucevi[pd.K_RIGHT]:
        if prethodno:
            if trenutnaPozicija < 6:
                trenutnaPozicija += 1
                tabla[0][trenutnaPozicija] = igrac
                tabla[0][trenutnaPozicija - 1] = None
        prethodno = False
            
    elif kljucevi[pd.K_SPACE]:
        if prethodno:
            if popunjeno[trenutnaPozicija] < 6:
                tabla[6 - popunjeno[trenutnaPozicija]][trenutnaPozicija] = igrac
                tabla[0][trenutnaPozicija] = None
                if igrac == proveri(tabla, 6 - popunjeno[trenutnaPozicija], trenutnaPozicija):
                    print()
                    print()
                    if igrac:
                        print("PLAVI IGRAC JE POBEDIO")
                    elif not igrac:
                        print("CRVENI JE POBEDIO")
                    print()
                    print()
                    break
                popunjeno[trenutnaPozicija] += 1
                igrac = not igrac
                tabla[0][trenutnaPozicija] = igrac
            

        prethodno = False
    
    else: prethodno = True
    
    if igrac: boja = "blue"
    else: boja = "red"

           
    x, y = 0, 0
    for red in tabla:
        for polje in red:
            if polje == None and y != 0:
                boja = "white"
            elif polje == None and y == 0:
                boja = "black"
            elif polje:
                boja = "blue"
            else:
                boja = "red"
            pd.draw.circle(ekran, boja, (120 * x + 60, 120 * y + 60), 50)
            x += 1
        y += 1
        x = 0
    pd.draw.line(ekran, "white", (0, 120), (840, 120))
 
    pd.display.flip()

endscr = True
while endscr:
    for event in pd.event.get():
        if event.type == pd.QUIT:
            endscr = not endscr
    
    for polje in tabla[0]: polje = None
    x, y = 0, 1
    for red in tabla[1:]:
        for polje in red:
            if polje == None:
                boja = "white"
            elif polje:
                boja = "blue"
            else:
                boja = "red"
            pd.draw.circle(ekran, boja, (120 * x + 60, 120 * y + 60), 50)
            x += 1
        y += 1
        x = 0
    

    pd.draw.line(ekran, "white", (0, 120), (840, 120))



    pd.display.flip()