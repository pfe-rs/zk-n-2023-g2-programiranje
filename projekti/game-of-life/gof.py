from time import sleep
import sys
from random import randint
import pygame

pygame.init()

xmax = 1280
ymax = 720
screen = pygame.display.set_mode((xmax, ymax), 0, 24)

def check(alive, neighbours):
    return neighbours == 3 or (alive and neighbours == 2)

def count_neighbours(grid, position):
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count


def make_grid(x, y):
        grid = []
        for r in range(x):
            row = []
            for c in range(y):
                row.append(randint(0,1))
            grid.append(row)
        return grid

def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

def update(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if check(cell, neighbours) else 0
    return new_grid

black = (0, 0, 0)

def draw(x, y, alive_color):
    block_size = 10
    x *= block_size
    y *= block_size

    center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
    pygame.draw.circle(screen, alive_color, center_point, block_size / 2)


def main():
    h = 0
    running = True

    alive_color = pygame.Color(0,0,0)

    xlen = int(xmax / 10)
    ylen = int(ymax / 10)

    while running:
       
        world = make_grid(xlen, ylen)

        for i in range(200):

            for x in range(xlen):
                for y in range(ylen):
                    alive = world[x][y]
                    cell_color = alive_color if alive else black
                    draw(x, y, cell_color)
            h = (h + 2) % 360
            alive_color.hsva = (h, 100, 100)
            world = update(world)
            sleep(0.1)
            pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



if __name__ == '__main__':
    main()
