with open('../input/day9_example.txt') as f:
    lines = f.readlines()

t_visited = {(0,0)}
head_coord = [0,0]
tail_coord_p1 = [0,0]
tail_coord_p2 = [0,0]
t_visited_p2 = {(0,0)}

knot_count = 10
knot_coord = []
for n in range(knot_count):
    knot_coord.append([0,0])

iter = 0
for line in lines:
    iter += 1
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
        prev_knot_coord = knot_coord[0]
        knot_coord[0] = [x + y for x, y in zip(knot_coord[0], delta)]
        for knot_n in range(1,10):
            if abs(knot_coord[knot_n-1][0] - knot_coord[knot_n][0]) == 2 or abs(knot_coord[knot_n-1][1] - knot_coord[knot_n][1]) == 2:
                temp = knot_coord[knot_n]
                knot_coord[knot_n] = prev_knot_coord
                prev_knot_coord = temp
                if knot_n == 1:
                    t_visited.add(tuple(knot_coord[knot_n]))
                if knot_n == 9:
                    t_visited_p2.add(tuple(knot_coord[knot_n]))
            else:
                break
    if (iter == 2):
        print(knot_coord)
        break
        
print("Part 1 : ",len(t_visited))
print("Part 2 : ",len(t_visited_p2))