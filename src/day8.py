with open('../input/day8.txt') as f:
    lines = f.readlines()

forest = []
for line in lines:
    row = [int(x) for x in line.strip()]
    forest.append(row)

def findfirst(list,query):
    index = 0
    len_list = len(list)
    while index < len_list and list[index] != query:
        index += 1
    return index if index == len(list) else index+1

visible_trees = (len(forest)-1) * 4
max_scenic_score = 0
for i in range(1,len(forest)-1):
    for j in range(1,len(forest[0]) -1):
        blocking_trees_right = [1 if x >= forest[i][j] else 0  for x in forest[i][j+1:]]
        blocking_trees_left = [1 if x >= forest[i][j] else 0  for x in forest[i][j-1::-1]]
        blocking_trees_up = [1 if x[j] >= forest[i][j] else 0  for x in forest[i-1::-1]]
        blocking_trees_down = [1 if x[j] >= forest[i][j] else 0  for x in forest[i+1:]]
        down_score = findfirst(blocking_trees_down,1)
        up_score = findfirst(blocking_trees_up,1)
        right_score = findfirst(blocking_trees_right,1)
        left_score = findfirst(blocking_trees_left,1)
        scenic_score = down_score * up_score * left_score * right_score
        max_scenic_score = max(scenic_score,max_scenic_score)
        if sum(blocking_trees_down) == 0 or sum(blocking_trees_up) == 0 or sum(blocking_trees_right) == 0 or sum(blocking_trees_left) == 0:
            visible_trees += 1

print("Part 1 : ",visible_trees)
print("Part 2 : ",max_scenic_score)
    