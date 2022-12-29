from queue import PriorityQueue

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

cur_pos = min(no_blizzards)
end_pos = max(no_blizzards)
walls.add((cur_pos[0] - 1,cur_pos[1]))
walls.add((end_pos[0] + 1,end_pos[1]))
x_wrap = end_pos[0]
y_wrap = end_pos[1]+1

cost_dict = dict()
for i in range(-2,x_wrap+2):
    for j in range(-2,y_wrap+2):
        cost_dict[(i,j)] = abs(end_pos[1]-j) + abs(end_pos[0]-i)

map_dict = dict()
for n in range(1000):
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
    map_dict[n] = blizzards_set    

def feasible_moves(pos,blizzards_set):
    moves = {(pos[0],pos[1]),(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)}
    new_moves =  moves & (moves ^ walls ^ blizzards_set)
    return new_moves

def dijkstra_search(start,goal,time):
    pq = PriorityQueue()
    pq.put((0,start,time))
    times = dict()
    visited = set()
    while not pq.empty():    
        current = pq.get()
        pos = current[1]
        time = current[2]
        if current[1] == goal:
            break
        if (pos,time) not in visited:
            visited.add((pos,time))
            neighbors = feasible_moves(current[1],map_dict[current[2]])
            new_time = time + 1
            for neighbor in neighbors:
                new_time = time + 1
                new_cost = cost_dict[neighbor] + time
                pq.put((new_cost,neighbor,new_time))
                times[neighbor] = new_time

    return times[goal]

time_p1 = dijkstra_search(cur_pos,end_pos,0)
print("Part 1 : ",time_p1)
time_p2 = dijkstra_search(cur_pos,end_pos,dijkstra_search(end_pos,cur_pos,time_p1))
print("Part 2 : ",time_p2)
        



