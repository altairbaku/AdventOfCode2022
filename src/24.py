with open('../input/24.txt') as f:
    lines = f.readlines()

blizzards = {'>':[],'<':[],'^':[],'v':[]}
no_blizzards = set()
walls = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char in blizzards.keys():
            blizzards[char].append((i-1,j-1))
        elif char == '.':
            no_blizzards.add((i-1,j-1))
        elif char == '#':
            walls.add((i-1,j-1))

def feasible_moves(pos,blizzards_set):
    moves = {(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)}
    new_moves =  moves & (moves ^ walls ^ blizzards_set)
    min_distance = 10000
    best_move = pos
    for move in new_moves:
        goal_distance = abs(move[0]-end_pos[0]) + abs(move[1]-end_pos[1])
        if goal_distance < min_distance:
            best_move = move
            min_distance = goal_distance
    return best_move


cur_pos = min(no_blizzards)
end_pos = max(no_blizzards)
print(cur_pos)
print(end_pos)
x_wrap = 20
y_wrap = 150

time = 0
while cur_pos != end_pos:
    blizzards_set = set()
    for k,v in blizzards.items():
        if k == '>':
            new_v = [(x[0],(x[1]+1) % y_wrap) for x in v]
        elif k == '<':
            new_v = [(x[0],(x[1]-1) % y_wrap) for x in v]
        elif k == '^':
            new_v = [((x[0]-1) % x_wrap,x[1]) for x in v]
        else:
            new_v = [((x[0]+1) % x_wrap,x[1]) for x in v]
        blizzards_set.update(set(new_v))
        blizzards[k] = new_v       
    cur_pos = feasible_moves(cur_pos,blizzards_set)
    time += 1

print(time)
        



