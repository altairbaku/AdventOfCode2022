with open('../input/10.txt') as f:
    lines = f.readlines()

cycle_number = 0
X = 1
X_vec = []
for line in lines:
    instruction = line.strip().split()
    if instruction[0] == 'addx':
        X_vec.extend([X,X])
        X += int(instruction[1])
    else:
        X_vec.append(X)
    
queries = [20,60,100,140,180,220]
p1 = 0
for query in queries:
    p1 += query * X_vec[query-1]

print("Part 1 : ",p1)

h = 6
w = 40
grid = [['.' for x in range(w)] for y in range(h)]
sprite_position = 1
for x in range(h):
    for y in range(w):
        if abs(X_vec[w*x + y]-y) <= 1:
            grid[x][y] = '#'
    print(''.join(grid[x][:]))

    

    
