import re
from copy import deepcopy

def rotate2d(vec,stheta):
    rot_vec = [0,0]
    rot_vec[0] = - stheta * vec[1]
    rot_vec[1] = stheta * vec[0] 
    return rot_vec

with open('../input/22_example.txt') as f:
    lines = f.readlines()

open_tiles = set()
solid_walls = set()
for i in range(len(lines) - 2):
    for j in range(len(lines[i]) - 1):
        if lines[i][j] == '.':
            open_tiles.add((-i,j))
        elif lines[i][j] == '#':
            solid_walls.add((-i,j))

full_map = open_tiles.union(solid_walls)
path = re.split('(\d+)', lines[len(lines)-1].strip())[1:-1]

pos = max(open_tiles)
step = [0,1]

for instruction in path:
    if instruction.isdigit():
        for n in range(int(instruction)):
            next_pos = tuple(map(sum, zip(pos, step)))
            if next_pos not in full_map:
                if next_pos[0] < pos[0] and next_pos[1] == pos[1]:
                    next_pos = max({element for element in full_map if element[1] == pos[1]})
                elif next_pos[0] > pos[0] and next_pos[1] == pos[1]:
                    next_pos = min({element for element in full_map if element[1] == pos[1]})
                elif next_pos[0] == pos[0] and next_pos[1] < pos[1]:
                    next_pos = max({element for element in full_map if element[0] == pos[0]})
                else:
                    next_pos = min({element for element in full_map if element[0] == pos[0]})
            
            if next_pos in solid_walls:
                break
            elif next_pos in open_tiles:
                pos = deepcopy(next_pos)

    elif instruction == 'R':
        step = rotate2d(step,1)
    else:
        step = rotate2d(step,-1)

print(1000 * (1 - pos[0]) + 4 * (pos[1]+ 1))




