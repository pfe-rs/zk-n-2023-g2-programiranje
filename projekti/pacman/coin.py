from hyperparameters import *
import pygame


class coin:
    def __init__(self, pos_x, pos_y, radius, color):
        self.pos_x = pos_x * SCALE_FACTOR
        self.pos_y = pos_y * SCALE_FACTOR
        self.radius = radius
        self.color = color
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)
    
coins = []
coin_color = (230, 243, 42)
#coins.append(coin())
for i in range(2, 20):
    coins.append(coin(2, i, 5, coin_color))

for i in range(2, 20):
    coins.append(coin(21, i, 5, coin_color))

for i in range(3, 21):
    coins.append(coin(i, 6, 5, coin_color))

for i in range(7, 15):
    coins.append(coin(6, i, 5, coin_color))

for i in range(3, 11):
    coins.append(coin(i, 15, 5, coin_color))

for i in range(13, 21):
    coins.append(coin(i, 15, 5, coin_color))

coins.append(coin(7, 2, 5, coin_color))
coins.append(coin(7, 3, 5, coin_color))
coins.append(coin(7, 4, 5, coin_color))
coins.append(coin(7, 5, 5, coin_color))

for i in range(8, 16):
    coins.append(coin(i, 3, 5, coin_color))

coins.append(coin(16, 2, 5, coin_color))
coins.append(coin(16, 3, 5, coin_color))
coins.append(coin(16, 4, 5, coin_color))
coins.append(coin(16, 5, 5, coin_color))

for i in range(7, 13):
    coins.append(coin(9, i, 5, coin_color))
for i in range(7, 13):
    coins.append(coin(14, i, 5, coin_color))

coins.append(coin(10, 12, 5, coin_color))
coins.append(coin(11, 12, 5, coin_color))
coins.append(coin(12, 12, 5, coin_color))
coins.append(coin(13, 12, 5, coin_color))

for i in range(7, 15):
    coins.append(coin(17, i, 5, coin_color))
coins.append(coin(7, 16, 5, coin_color))
coins.append(coin(7, 17, 5, coin_color))
coins.append(coin(7, 18, 5, coin_color))
coins.append(coin(7, 19, 5, coin_color))

coins.append(coin(16, 16, 5, coin_color))
coins.append(coin(16, 17, 5, coin_color))
coins.append(coin(16, 18, 5, coin_color))
coins.append(coin(16, 19, 5, coin_color))

coins.append(coin(10, 16, 5, coin_color))
coins.append(coin(10, 17, 5, coin_color))

coins.append(coin(11, 17, 5, coin_color))
coins.append(coin(12, 17, 5, coin_color))

coins.append(coin(13, 16, 5, coin_color))
coins.append(coin(13, 17, 5, coin_color))

"""
coins.append(coin(3, 4, 5, (255, 0, 0)))
coins.append(coin(4, 4, 5, (255, 0, 0)))
coins.append(coin(5, 4, 5, (255, 0, 0)))
coins.append(coin(6, 4, 5, (255, 0, 0)))"""
"""coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())
coins.append(coin())"""


