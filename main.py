from setup import *
import time
import os
import pygame as pg
import numpy as np

pg.init()
flags = pg.FULLSCREEN | pg.SCALED
screen = pg.display.set_mode((1920, 1080), flags)
clock = pg.time.Clock()



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
"""
input = input("1. blinker, 2.beacon, 3.random(20,20)\n")
match input:
    case "1":
        game_map = game_map_blinker
    case "2":
        game_map = game_map_beacon
    case default:
        game_map = size_map(20,20)
        game_map = pop_map(game_map)
"""
colours = np.array([[120, 250, 90], [250, 90, 120]])

# display_map(update_board(game_map,update))
# game_map = size_map(30,30)
# game_map = pop_map(game_map)
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
game_map = size_map(200,200)
game_map = pop_map(game_map)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    game_map = np.array(game_map)
    surface = pg.surfarray.make_surface(colours[game_map])
    surface = pg.transform.scale(surface, (800,800))
    screen.fill((30,30,30))
    screen.blit(surface,(100,100))
    pg.display.update()
    clock.tick(60)
    display_map(game_map)
    game_map = update_board(game_map, one_lifetime(game_map))
    clear()
