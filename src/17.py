from collections import deque,defaultdict

with open('../input/17.txt') as f:
    lines = f.readlines()

for line in lines:
    jet_list = [x for x in line.strip()]
    indices = list(range(len(jet_list)))
    jet_pattern = dict(zip(indices,jet_list))

rock_shapes = deque([lambda x1 : {(2,x1+4),(3,x1+4),(4,x1+4),(5,x1+4)},
                    lambda x2: {(2,x2+5),(3,x2+6),(3,x2+5),(3,x2+4),(4,x2+5)},
                    lambda x3 : {(2,x3+4),(3,x3+4),(4,x3+4),(4,x3+5),(4,x3+6)},
                    lambda x4 : {(2,x4+4),(2,x4+5),(2,x4+6),(2,x4+7)},
                    lambda x5 : {(2,x5+4),(3,x5+4),(2,x5+5),(3,x5+5)}])

rocks = 0
highest_rock = 0
jet_index = 0
total_jets = len(jet_pattern)
width = 7
fallen_rocks = {(i,0) for i in range(width)}

jet_dict = defaultdict(int)
print(total_jets)
repeating = 40
max_height = 0
while rocks < 1000:
    current_rock = rock_shapes[0](highest_rock)
    while True:
        if jet_pattern[jet_index] == '<':
            jet_move ={(x[0]-1,x[1]) for x in current_rock}
        else:
            jet_move ={(x[0]+1,x[1]) for x in current_rock}
        if not jet_move.intersection(fallen_rocks) and max(jet_move)[0] < 7 and min(jet_move)[0] >= 0:
            current_rock = jet_move
        jet_index = (jet_index + 1) % total_jets
        down_move = {(x[0],x[1] - 1) for x in current_rock}
        if not down_move.intersection(fallen_rocks) and min(down_move,key = lambda y : y[1])[1] > min(fallen_rocks,key = lambda y : y[1])[1]:
            current_rock = down_move
        else:
            temp_rocks = fallen_rocks | current_rock
            fallen_rocks = {x for x in temp_rocks if x[1] >= (highest_rock - 57)}
            highest_rock = max(fallen_rocks, key= lambda x : x[1])[1]
            break
    rocks += 1
    jet_dict[jet_index] += 1
    if rocks % repeating == 0:
        print(highest_rock - max_height)
        max_height = highest_rock
    rock_shapes.rotate(-1)

print(max(fallen_rocks, key= lambda x : x[1])[1])