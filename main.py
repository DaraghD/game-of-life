from setup import *
import time
import os

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

input = input("1. blinker, 2.beacon, 3.random(20,20)\n")
match input:
    case "1":
        game_map = game_map_blinker
    case "2":
        game_map = game_map_beacon
    case default:
        game_map = size_map(20,20)
        game_map = pop_map(game_map)

# display_map(update_board(game_map,update))
# game_map = size_map(30,30)
# game_map = pop_map(game_map)
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


while True:
    display_map(game_map)
    game_map = update_board(game_map, one_lifetime(game_map))
    time.sleep(2)
    clear()
