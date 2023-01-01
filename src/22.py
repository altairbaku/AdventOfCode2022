import re
import math

with open('../input/22.txt') as f:
    lines = f.readlines()

open_tiles = set()
solid_walls = set()
board_size = len(lines)-2
for x in range(board_size):
    ylim = len(lines[x]) - 1
    for y in range(ylim):
        col = y + 1
        if lines[x][y] == '.':
            open_tiles.add((x+1,y+1))
        elif lines[x][y] == '#':
            solid_walls.add((x+1,y+1))

full_map = open_tiles.union(solid_walls)
path = re.split('(\d+)', lines[len(lines)-1].strip())[1:-1]

facing = {(0,1) : 0, (0,-1) : 2, (1,0) : 1, (-1,0) : 3}

def rotate2d(vec,stheta):
    rot_vec = [0,0]
    rot_vec[0] =  stheta * vec[1]
    rot_vec[1] = - stheta * vec[0] 
    return rot_vec

def rotate3d(vec,theta,axis):
    rot_vec = [0,0,0]
    if axis == 'X':
        rot_vec[0] = vec[0]
        rot_vec[1] = round(math.cos(math.radians(theta)) * vec[1] + math.sin(math.radians(theta)) * vec[2])
        rot_vec[2] = round(math.cos(math.radians(theta)) * vec[2] - math.sin(math.radians(theta)) * vec[1])
    elif axis == 'Y':
        rot_vec[1] = vec[1]
        rot_vec[0] = round(math.cos(math.radians(theta)) * vec[0] - math.sin(math.radians(theta)) * vec[2])
        rot_vec[2] = round(math.cos(math.radians(theta)) * vec[2] + math.sin(math.radians(theta)) * vec[0])
    elif axis == 'Z':
        rot_vec[2] = vec[2]
        rot_vec[0] = round(math.cos(math.radians(theta)) * vec[0] + math.sin(math.radians(theta)) * vec[1])
        rot_vec[1] = round(math.cos(math.radians(theta)) * vec[1] - math.sin(math.radians(theta)) * vec[0])
    return rot_vec

def traverse_board():
    pos = min(set(filter(lambda x:x[0] == 1,open_tiles)))
    step = [0,1]
    for instruction in path:
        if instruction.isdigit():
            for _n in range(int(instruction)):
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
                    pos = next_pos
        elif instruction == 'R':
            step = rotate2d(step,1)
        else:
            step = rotate2d(step,-1)
    return (1000 * pos[0] + 4 * pos[1] + facing[tuple(step)])

def rot_angle(cur_step,cur_pos,cube_len):
    if cur_pos[0] == 0:
        if cur_step == [0,0,-1] or cur_step == [0,1,0]:
            return 90
        else:
            return -90
    if cur_pos[0] == cube_len:
        if cur_step == [0,0,-1] or cur_step == [0,1,0]:
            return -90
        else:
            return 90
    if cur_pos[1] == 0:
        if cur_step == [0,0,1] or cur_step == [-1,0,0]:
            return 90
        else:
            return -90
    if cur_pos[1] == cube_len:
        if cur_step == [0,0,1] or cur_step == [-1,0,0]:
            return -90
        else:
            return 90
    if cur_pos[2] == 0:
        if cur_step == [1,0,0] or cur_step == [0,-1,0]:
            return -90
        else:
            return 90
    if cur_pos[2] == -cube_len:
        if cur_step == [1,0,0] or cur_step == [0,-1,0]:
            return 90
        else:
            return -90

def traverse_cube(cube_side):
    open_tiles_3d = {(x[0],x[1]) : (x[0] - cube_side,x[1] - cube_side,0) for x in full_map}
    start_pos = min(set(filter(lambda x:x[0] == 1,open_tiles)))
    step = [0,1,0]
    for (k,v) in open_tiles_3d.items():
        if v[0] <= 0:
            open_tiles_3d[k] = (v[0]-1,v[1],v[2])
        if v[1] <= 0:
            open_tiles_3d[k] = (v[0],v[1]-1,v[2])

    foldable_tiles = dict(filter(lambda x : x[1][1] > cube_side,open_tiles_3d.items()))
    for (k,v) in foldable_tiles.items():
        open_tiles_3d[k] = tuple(map(sum,zip(rotate3d(v,90,'X'),[0,cube_side + 1,cube_side])))
        if k == start_pos:
            step = rotate3d(step,90,'X')

    foldable_tiles = dict(filter(lambda x : x[1][1] < 0,open_tiles_3d.items()))
    for (k,v) in foldable_tiles.items():
        open_tiles_3d[k] = tuple(rotate3d(v,-90,'X'))
        if k == start_pos:
            step = rotate3d(step,-90,'X')

    foldable_tiles = dict(filter(lambda x : x[1][0] > cube_side,open_tiles_3d.items()))
    for (k,v) in foldable_tiles.items():
        open_tiles_3d[k] = tuple(map(sum,zip(rotate3d(v,-90,'Y'),[cube_side+1,0,cube_side])))
        if k == start_pos:
            step = rotate3d(step,-90,'Y')

    foldable_tiles = dict(filter(lambda x : x[1][0] < 0,open_tiles_3d.items()))
    for (k,v) in foldable_tiles.items():
        open_tiles_3d[k] = tuple(rotate3d(v,90,'Y'))
        if k == start_pos:
            step = rotate3d(step,90,'Y')

    foldable_tiles = dict(filter(lambda x : x[1][2] < -cube_side,open_tiles_3d.items()))
    for (k,v) in foldable_tiles.items():
        open_tiles_3d[k] = tuple(map(sum,zip(rotate3d(v,-90,'X'),[0,-cube_side,-cube_side - 1])))
        if k == start_pos:
            step = rotate3d(step,-90,'X')

    open_tiles_2d = {v:k for k,v in open_tiles_3d.items()}
    pos = open_tiles_3d[start_pos]
    axis = ['X','Y','Z']
    cube_limit = cube_side + 1
    for instruction in path:
        if instruction.isdigit():
            for _n in range(int(instruction)):
                next_pos = tuple(map(sum, zip(pos, step)))
                if next_pos not in open_tiles_2d:
                    prev_step = step
                    test = [index for index,value in enumerate(next_pos) if value != 0 and value != cube_limit and value != -cube_limit]   
                    ang = rot_angle(step,pos,cube_limit)
                    step = rotate3d(step,ang,axis[test[0]])
                    next_pos = tuple(map(sum, zip(next_pos, step)))
                    if open_tiles_2d[next_pos] in solid_walls:
                        step = prev_step
                if open_tiles_2d[next_pos] in solid_walls:
                    break
                pos = next_pos
        elif instruction == 'R':
            test = [index for index,value in enumerate(pos) if value == 0 or value == cube_limit or value == -cube_limit]
            if pos[0] == 0 or pos[1] == 0 or pos[2] == -cube_limit:
                step = rotate3d(step,-90,axis[test[0]])
            else:
                step = rotate3d(step,90,axis[test[0]])
        else:
            test = [index for index,value in enumerate(pos) if value == 0 or value == cube_limit or value == -cube_limit]
            if pos[0] == 0 or pos[1] == 0 or pos[2] == -cube_limit:
                step = rotate3d(step,90,axis[test[0]])
            else:
                step = rotate3d(step,-90,axis[test[0]])

    cur_step = open_tiles_2d[pos]
    next_step = open_tiles_2d[tuple(map(sum, zip(pos, step)))]
    step_2d = tuple(map(lambda i, j: i - j, next_step, cur_step))
    return (1000 * open_tiles_2d[pos][0] + 4 * open_tiles_2d[pos][1] + facing[step_2d])

print("Part 1 : ",traverse_board())
print("Part 2 : ",traverse_cube(50))










