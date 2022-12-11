from itertools import product

with open('../input/day9.txt') as f:
    lines = f.readlines()

t_visited_p1 = {(0,0)}
t_visited_p2 = {(0,0)}

knot_count = 10
knot_coord = []
for n in range(knot_count):
    knot_coord.append([0,0])

def best_pos(head,tail):
    neighbors_1 = set(product(range(head[0]-1,head[0]+2),range(head[1]-1,head[1]+2)))
    neighbors_2 = set(product(range(tail[0]-1,tail[0]+2),range(tail[1]-1,tail[1]+2)))
    common_neighbors = list(neighbors_1.intersection(neighbors_2))
    dist = [abs(head[0]-x[0])+abs(head[1] - x[1]) for x in common_neighbors]
    min_index=dist.index(min(dist))
    return common_neighbors[min_index]

for line in lines:
    steps = int(line.split(" ")[1])
    if line[0] == 'R':
        delta = [1,0]
    elif line[0] == 'L':
        delta = [-1,0]
    elif line[0] == 'U':
        delta = [0,1]
    else:
        delta = [0,-1]

    for n in range(steps):
        knot_coord[0] = [x + y for x, y in zip(knot_coord[0], delta)]
        for knot_n in range(1,10):
            if abs(knot_coord[knot_n-1][0] - knot_coord[knot_n][0]) >= 2 or abs(knot_coord[knot_n-1][1] - knot_coord[knot_n][1]) >= 2:
                knot_coord[knot_n] = best_pos(knot_coord[knot_n-1],knot_coord[knot_n])
                if knot_n == 1:
                    t_visited_p1.add(tuple(knot_coord[knot_n]))
                if knot_n == 9:
                    t_visited_p2.add(tuple(knot_coord[knot_n]))

print("Part 1 : ",len(t_visited_p1))
print("Part 2 : ",len(t_visited_p2))