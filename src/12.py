from collections import defaultdict, deque
with open('../input/12.txt') as f:
    lines = f.readlines()

grid = []
row = 0
start_pos = tuple()
end_pos = tuple()
for line in lines:
    current_row = list(line.strip())
    grid.append([ord(x) for x in current_row])
    if not start_pos:
        for col in range(len(current_row)):
            if current_row[col] == 'S':
                start_pos = tuple([row,col])
    if not end_pos:
        for col in range(len(current_row)):
            if current_row[col] == 'E':
                end_pos = tuple([row,col])
    row += 1

def find_neighbors(pos,grid):
    up = pos[0] - 1
    down = pos[0] + 1
    left = pos[1] - 1
    right = pos[1] + 1
    neighbors = []
    if up >= 0 and grid[up][pos[1]] <= (grid[pos[0]][pos[1]] + 1):
        neighbors.append(tuple([up,pos[1]]))
    if down < len(grid) and grid[down][pos[1]] <= (grid[pos[0]][pos[1]] + 1):
        neighbors.append(tuple([down,pos[1]]))
    if left >= 0 and grid[pos[0]][left] <= (grid[pos[0]][pos[1]] + 1):
        neighbors.append(tuple([pos[0],left]))
    if right < len(grid[0]) and grid[pos[0]][right] <= (grid[pos[0]][pos[1]] + 1):
        neighbors.append(tuple([pos[0],right]))
    return neighbors

def estimate_steps(visited,yet_to_visit,grid,end_pos):
    while True:
        if not yet_to_visit:
            break
        cur_node = yet_to_visit.popleft()
        neighbors = find_neighbors(cur_node,grid)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = visited[cur_node] + 1
                yet_to_visit.append(neighbor)
    if end_pos in visited.keys():
        return visited[end_pos]
    else:
        return 10000

grid[start_pos[0]][start_pos[1]] = ord('a')
grid[end_pos[0]][end_pos[1]] = ord('z')

start_positions = []
lowest_elevation = ord('a')
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == lowest_elevation:
            start_positions.append(tuple([i,j]))

min_steps = len(grid) * len(grid[0])
for x in start_positions:
    visited = defaultdict()
    visited[x] = 0
    yet_to_visit = deque()
    yet_to_visit.append(x)
    steps = estimate_steps(visited,yet_to_visit,grid,end_pos)
    if x == start_pos:
        print("Part 1 : ",steps)
    min_steps = min(min_steps,steps)

print("Part 2 : ",min_steps)