import random
import time


def size_map(row: int, col: int):  # only use same number for eahc one xDd
    map = [[0 for col in range(col)] for row in range(row)]

    return map


def pop_map(map):  # populates map
    for row in range(len(map)):
        for col in range(len(map[row])):
            x = random.randrange(1,5,1)

            if x == 1:
                map[row][col] = 1  # live cell
            else:
                map[row][col] = 0

    return map


def display_map(map):
    for row in range(len(map)):
        print(map[row])
        for col in range(len(map[row])):
            if col == len(map[row]):
                print("\n")
                continue


def apply_rule(map, y, x) -> int:
    neighbours = 0
    flagxp = False  # flags so we dont go out of index range
    flagxm = False
    flagyp = False
    flagym = False
    lenM = len(map) - 1  # -1 cause we indexing

    if x + 1 > lenM:
        flagxp = True
    if x - 1 < 0:
        flagxm = True
    if y + 1 > lenM:
        flagyp = True
    if y - 1 < 0:
        flagym = True

    if map[y + 1][x + 1] == 1:
        neighbours += 1

    if map[y + 1][x] == 1:
        neighbours += 1

    if map[y - 1][x - 1] == 1:
        neighbours += 1

    if map[y - 1][x] == 1:
        neighbours += 1

    if map[y][x - 1] == 1:
        neighbours += 1

    if map[y][x + 1] == 1:
        neighbours += 1

    if map[y - 1][x + 1] == 1:
        neighbours += 1

    if map[y + 1][x - 1] == 1:
        neighbours += 1

    return neighbours


test_map = [[0, 0, 0, 0, 0],  # should be a blinker
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]


def one_lifetime(map):
    pointerx: int = 0
    pointery: int = 0
    new_cell: list = []
    dead_cell: list = []
    len_end = len(map) - 1
    for row in range(0, len(map), 1):
        for col in range(0, len(map), 1):
            try:
                neighbours = apply_rule(map, row, col)
            except IndexError:
                dead_cell.append(row)
                dead_cell.append(col)

                continue
            if map[row][col] == 0:
                neighbours = apply_rule(map, row, col)
                if neighbours == 3:
                    new_cell.append(row)
                    new_cell.append(col)
            else:
                if neighbours < 2:
                    dead_cell.append(row)
                    dead_cell.append(col)
                if neighbours > 3:
                    dead_cell.append(row)
                    dead_cell.append(col)
                #if neighbours == 3:
                #    new_cell.append(row)
                 #   new_cell.append(col)
    return new_cell,dead_cell

# first tuple from one_lifetime is new_cell, second is dead ones
def update_board(map: list[list], update: tuple) -> list[list]:
    (new_cells, dead_cells) = update
    len_dead = (int(len(dead_cells)))
    for i in range(0, len(new_cells), 2):
        map[new_cells[i]][new_cells[i + 1]] = 1
    for j in range(0, len(dead_cells), 2):
        map[dead_cells[j]][dead_cells[j+1]] =0

    return map


def find_pop(map) -> int:
    population = 0
    for row in range(0, len(map), 1):
        for col in range(0, len(map), 1):
            if map[row][col] == 1:
                population += 1
    return population


