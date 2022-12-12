with open('../input/day12.txt') as f:
    lines = f.readlines()

grid = []
row = 0
start_pos = []
for line in lines:
    current_row = list(line.strip())
    grid.append(current_row)
    if not start_pos:
        for col in range(len(current_row)):
            if current_row[col] == 'S':
                start_pos.extend([row,col])
    row += 1

