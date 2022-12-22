import re

def rotate2d(vec,stheta):
    rot_vec = [0,0]
    rot_vec[0] = - stheta * vec[1]
    rot_vec[1] = stheta * vec[0] 
    return rot_vec

with open('../input/22.txt') as f:
    lines = f.readlines()

open_tiles = set()
solid_walls = set()
for i in range(len(lines) - 2):
    for j in range(len(lines[i]) - 1):
        if lines[i][j] == '.':
            open_tiles.add((i,j))
        elif lines[i][j] == '#':
            solid_walls.add((i,j))

full_map = open_tiles.union(solid_walls)
print(len(full_map))
path = re.split('(\d+)', lines[len(lines)-1].strip())[1:-1]

pos = min(open_tiles)
step = [1,0]

for instruction in path:
    if instruction.isdigit():
        for n in range(int(instruction)):
            next_pos = tuple(map(sum, zip(pos, step)))
            if next_pos not in full_map:
                if next_pos[0] == pos[0] and next_pos[1] < pos[1]:
                    print("A")

            if next_pos in solid_walls:
                break
            elif next_pos in open_tiles:
                pos = next_pos

    elif instruction == 'R':
        step = rotate2d(step,-1)
    else:
        step = rotate2d(step,1)




