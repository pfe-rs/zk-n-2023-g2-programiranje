import pygame
import numpy as np
import random
import Scene
import time





scena = Scene.SveScene()
teraj = True
scena.PocetniEkran()
time.sleep(2)
scena.UI()
scena.number_of_tiles = 10

while teraj:

    try:
        scena.Glavna()
        teraj = scena.ProveraZavrsen()
    except KeyboardInterrupt:
        print("aaaaa")
        teraj = False
    b = scena.ProveraPobede()
    teraj = teraj and b
    #x += tank_speed

if b:
    scena.ZavrsniEkran()
else:
    scena
time.sleep(2)


pygame.quit()

