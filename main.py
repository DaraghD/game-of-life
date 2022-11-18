from setup import *
import time
import os
import pygame as pg
import numpy as np

print("Conways game of life,simple rules very interesting results\nmap will be randomly populated,\nalt tab to pygame window\n")
size = int(input("enter the amount of tiles u want: "))
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
colours = np.array([[0, 0, 0], [250, 90, 120]])

# display_map(update_board(game_map,update))
# game_map = size_map(30,30)
# game_map = pop_map(game_map)
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


game_map=size_map(size,size)
game_map = pop_map(game_map)

pg.init()
flags = pg.SCALED
screen = pg.display.set_mode((1000, 1000), flags)
clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    game_map = np.array(game_map)
    surface = pg.surfarray.make_surface(colours[game_map])
    surface = pg.transform.scale(surface, (1200,1200))
    screen.fill((30,30,30))
    screen.blit(surface,(100,100))
    pg.display.update()
    clock.tick(60)
    display_map(game_map)
    if speed != 0:
        time.sleep(speed)
    game_map = update_board(game_map, one_lifetime(game_map))
    clear()
