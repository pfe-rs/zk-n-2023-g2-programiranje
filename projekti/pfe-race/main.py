import pygame as pg
from car import Car
SCREEN_DIM = 512
OFFSET = 20
SPEED = 16

pg.font.init()
PFEColor = (0, 153, 153)
roadClr = (64, 64, 64)
running = True
screen = pg.display.set_mode((SCREEN_DIM, SCREEN_DIM))
car1 = Car((0, 0, 0), SPEED, 50+OFFSET, 246+OFFSET)
car2 = Car((45, 78, 145), SPEED*1.25, car1.sprite.left, car1.sprite.top+64)
pal = pg.time.Clock()
put = pg.Rect(20, 20, SCREEN_DIM-40, SCREEN_DIM-40)
nedostupnaPolja = list()
nedostupnaPolja.append(pg.Rect(128+OFFSET, 128+OFFSET, 236, 236)) #PFE glava
nedostupnaPolja.append(pg.Rect(96+OFFSET, 288+OFFSET, 300, 16)) # PFE ruke
for i in range(198, 279, 40):
    nedostupnaPolja.append(pg.Rect(i+OFFSET,364+OFFSET, 16, 64))
frames = 0
while running:
    screen.fill(PFEColor)
    pg.draw.rect(screen, roadClr, put)
    for nedostupnoPojle in nedostupnaPolja:
        pg.draw.rect(screen, PFEColor, nedostupnoPojle)
    pg.draw.circle(screen, "white",(256, 256), 32)
    pg.draw.circle(screen, "black",(256, 256), 8)
    pal.tick(25)
    frames += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    mousePosition = pg.mouse.get_pos()
    
    car1.move(mousePosition[0], mousePosition[1])
    car2.move(car1.sprite.left, car1.sprite.top)
    car1.draw(screen)
    car2.draw(screen)

    if(pg.Rect.colliderect(car1.sprite, car2.sprite) or not pg.Rect.colliderect(car1.sprite, put)):
        running = False
    for nedostupnoPolje in nedostupnaPolja:
        if(pg.Rect.colliderect(car1.sprite, nedostupnoPolje)):
            running = False
            
    if (running == False):
        font = pg.font.Font(None, 32)
        text = font.render("Sad idi autobusom do Tršića", True, (10, 10, 10))
        textpos = text.get_rect(centerx=SCREEN_DIM / 2, y=32)
        screen.blit(text, textpos)
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                     pg.quit()
        

    if(frames%250==0):
        car2.speed += 0.01

    pg.display.flip()   