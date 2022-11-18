import string

from setup import *
import time
import pygame as pg
import numpy as np
from graph import *


print("Conways game of life,simple rules very interesting results\nmap will be randomly populated,\nalt tab to pygame window\n")
choice = int(input("1: Blinker map\n2: Beacon map\n3: Penta decathlon \n4: make own random map\n"))

if choice == 4:
    size = int(input("enter the amount of tiles u want:\n "))
speed = float(input("Enter amount of seconds in between each lifetime, recommended 0.5\n"))

game_map_blinker \
    = [[0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0]]

game_map_beacon = \
    [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

pentamap = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



if choice ==1:
    game_map = game_map_blinker
elif choice == 2:
    game_map = game_map_beacon
elif choice == 3:
    game_map = pentamap
else:
    game_map=size_map(size,size)
    game_map = pop_map(game_map)

pg.init()
colours = np.array([[0, 0, 0], [200, 20, 100]])
flags = pg.SCALED | pg.FULLSCREEN
screen = pg.display.set_mode((1920, 1080), flags)
clock = pg.time.Clock()

pg.font.init()
my_font = pg.font.SysFont('Arial', 30)


populationlist = []
lifecycle = []
lifecyclecounter =0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            graph_era(populationlist,lifecycle)
            exit()
    game_map = np.array(game_map)
    population = find_pop(game_map)
    population_string = "Population : "+str(population)
    surface = pg.surfarray.make_surface(colours[game_map])
    surface = pg.transform.scale(surface, (900, 900))

    text_surface = my_font.render(population_string,False,(250,250,250))
    screen.fill("black")
    screen.blit(text_surface, (0, 0))
    screen.blit(surface, (0, 40))

    pg.display.flip()


    clock.tick(10)
    if speed != 0:
        time.sleep(speed)

    populationlist.append(population)
    lifecyclecounter += 1
    lifecycle.append(lifecyclecounter)
    game_map = update_board(game_map, one_lifetime(game_map))
    print(game_map)

