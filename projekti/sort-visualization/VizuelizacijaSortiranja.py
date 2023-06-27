import pygame
import random
import time
pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_ELEM = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
a = []
white = (225, 225, 225)
red = (225, 0, 0)
green = (0, 255, 0)

for i in range(NUM_ELEM):
    a.append(1+i*SCREEN_HEIGHT/NUM_ELEM)

random.shuffle(a)

bar_width = SCREEN_WIDTH/NUM_ELEM
running=True

def draw_array (a, i, j):
    for x in range(len(a)):
        if x == i or x == j:
            pygame.draw.rect(screen, red , pygame.Rect(x*bar_width, SCREEN_HEIGHT-a[x], bar_width-1, a[x]))
        else: 
            pygame.draw.rect(screen, white , pygame.Rect(x*bar_width, SCREEN_HEIGHT-a[x], bar_width-1, a[x]))


def draw_array_check (a, i):
    for x in range(len(a)):
        if x == i:
            pygame.draw.rect(screen, green , pygame.Rect(x*bar_width, SCREEN_HEIGHT-a[x], bar_width-1, a[x]))
        else: 
            pygame.draw.rect(screen, white , pygame.Rect(x*bar_width, SCREEN_HEIGHT-a[x], bar_width-1, a[x]))


def SELECTION_SORT(a):
    pygame.display.flip()
    screen.fill((0,0,0))
    write("Selection sort", font, white, 0, 0)
    draw_array(a, -1, -1)
    for i in range (NUM_ELEM-1):
        min_idx = i
        for j in range (i+1, NUM_ELEM): 
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Selection sort", font, white, 0, 0)
            draw_array(a, i, j)
            if a[j] < a[min_idx]: min_idx = j
        if min_idx != i:
            p = a[min_idx]
            a[min_idx]=a[i]
            a[i]=p
    pygame.display.flip()
    screen.fill((0,0,0))
    write("Selection sort", font, white, 0, 0)

def INSERTION_SORT(a):
    pygame.display.flip()
    screen.fill((0,0,0))
    write("Insertion sort sort", font, white, 0, 0)
    draw_array(a, -1, -1)
    for step in range(1, len(a)):
        key = a[step]
        j = step - 1        
        while j >= 0 and key < a[j]:
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Insertion sort", font, white, 0, 0)
            draw_array(a, i, j)
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


def partition(a, l, r):

  pivot = a[r]
  i = l - 1
  for j in range(l, r):
    screen.fill((0,0,0))
    write("Quick sort", font, white, 0, 0)
    draw_array(a, i, j)
    pygame.display.flip()
    if a[j] <= pivot:
      i = i + 1
      (a[i], a[j]) = (a[j], a[i])
  (a[i + 1], a[r]) = (a[r], a[i + 1])
  return i + 1

def QUICK_SORT(a, l, r):
  if l < r:
    pi = partition(a, l, r)
    QUICK_SORT(a, l, pi - 1)
    QUICK_SORT(a, pi + 1, r)


def SHELL_SORT(a, n):
    pygame.display.flip()
    screen.fill((0,0,0))
    write("Shell sort", font, white, 0, 0)
    draw_array(a, -1, -1)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = a[i]
            j = i
            while j >= interval and a[j - interval] > temp:
                pygame.display.flip()
                screen.fill((0,0,0))
                write("Shell sort", font, white, 0, 0)
                draw_array(a, i, j)
                a[j] = a[j - interval]
                j -= interval

            a[j] = temp
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Shell sort", font, white, 0, 0)
            draw_array(a, i, j)
        interval //= 2

def BUBBLE_SORT (a):
    for i in range(len(a)):
        for j in range (len(a)-i-1):
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Bubble sort", font, white, 0, 0)
            draw_array(a, j+1, j)
            if (a[j]>a[j+1]): 
                (a[j], a[j+1]) = (a[j+1], a[j])

def COCKTAIL_SORT (a):
    n = len(a)
    swapped = True
    l = 0
    r = n-1
    while (swapped == True):
        swapped = False
        for i in range (l, r):
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Cocktail sort", font, white, 0, 0)
            draw_array(a, i+1, i)
            if a[i] > a[i+1]:
                (a[i], a[i+1]) = (a[i+1], a[i])
        if swapped == False: 
            break 
        swapped = False 
        r = r-1
        for i in range(r-1, l-1, -1):
            pygame.display.flip()
            screen.fill((0,0,0))
            write("Cocktail sort", font, white, 0, 0)
            draw_array(a, i+1, i)
            if (a[i] > a[i + 1]):
                (a[i], a[i + 1]) = (a[i + 1], a[i])
                swapped = True
        l = l+1

def GNOME_SORT(arr):
    n = len(arr)
    index = 0

    while index < n:
        pygame.display.flip()
        screen.fill((0,0,0))
        write("Gnome sort", font, white, 0, 0)
        draw_array(a, index+1, index)
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp 
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]
        pygame.display.flip()
        screen.fill((0,0,0))
        write("Radix sort LSD", font, white, 0, 0)
        draw_array(arr, i, -1)
        time.sleep(0.1)

def RADIX_SORT_LSD(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def CYCLE_SORT(array):
  writes = 0
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
        pygame.display.flip()
        screen.fill((0,0,0))
        write("Cycle sort", font, white, 0, 0)
        draw_array(a, i, cycleStart)
        if array[i] < item:
            pos += 1
    if pos == cycleStart:
      continue
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
    while pos != cycleStart:
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1

font = pygame.font.SysFont("Arial", 32)

def write (text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


while running: 
    pygame.display.flip()
    screen.fill((0,0,0))
    clock.tick(1) 
    SELECTION_SORT(a)
    random.shuffle(a)
    INSERTION_SORT(a)
    random.shuffle(a)
    QUICK_SORT(a, 0, NUM_ELEM-1)
    random.shuffle(a)
    SHELL_SORT(a, NUM_ELEM)
    random.shuffle(a)
    BUBBLE_SORT(a)
    random.shuffle(a)
    GNOME_SORT(a)
    random.shuffle(a)
    RADIX_SORT_LSD(a)
    random.shuffle(a)
    CYCLE_SORT(a)
    pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()