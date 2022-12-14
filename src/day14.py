from itertools import product
from copy import deepcopy

with open('../input/day14.txt') as f:
    rock_paths = f.readlines()

rock_indices = set()
for rock_path in rock_paths:
    rock_line = rock_path.strip().split(' -> ')
    for n in range(0,len(rock_line)-1):
        coord_1 = rock_line[n].split(',')
        coord_2 = rock_line[n+1].split(',')
        x = [int(coord_1[0]),int(coord_2[0])]
        y = [int(coord_1[1]),int(coord_2[1])]
        rock_list = list(product(range(min(x),max(x)+1),range(min(y),max(y)+1)))
        for rock in rock_list:
            rock_indices.add(rock)

lowest = max([x[1] for x in rock_indices])
sand_units = 0
flow = 0
rock_indices_p1 = deepcopy(rock_indices)
while not flow:
    sand_coord = (500,0)
    at_rest = 0
    while not at_rest:
        down = sand_coord[1] + 1
        left = sand_coord[0] - 1
        right = sand_coord[0] + 1
        possible_moves = [(sand_coord[0],down), (left,down),(right,down)]
        moved = 0
        for move in possible_moves:
            if move not in rock_indices_p1:
                sand_coord = move
                moved = 1
                break
        if moved == 0:
            sand_units += 1
            rock_indices_p1.add(sand_coord)
            at_rest = 1
        if sand_coord[1] > lowest:
            flow = 1
            break
print(sand_units)

sand_coord = (0,0)
floor = lowest + 2
sand_units_p2 = 0
while sand_coord != (500,0):
    sand_coord = (500,0)
    at_rest = 0
    while not at_rest:
        down = sand_coord[1] + 1
        left = sand_coord[0] - 1
        right = sand_coord[0] + 1
        possible_moves = [(sand_coord[0],down), (left,down),(right,down)]
        moved = 0
        for move in possible_moves:
            if move not in rock_indices and move[1] <= floor-1:
                sand_coord = move
                moved = 1
                break
        if moved == 0:
            sand_units_p2 += 1
            rock_indices.add(sand_coord)
            at_rest = 1
        if sand_coord == (500,0):
            break

print(sand_units_p2)





