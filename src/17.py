from collections import deque

with open('../input/17_example.txt') as f:
    lines = f.readlines()

for line in lines:
    jet_pattern = [x for x in line.strip()]

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
while rocks < 2022:
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
            print(current_rock)
            temp_rocks = fallen_rocks | current_rock
            print(temp_rocks)
            fallen_rocks = set()
            for j in range(width):
                new_floor = {x for x in temp_rocks if x[0] == j}
                fallen_rocks.add(max(new_floor,key = lambda y : y[1]))
            print(fallen_rocks)
            highest_rock = max(fallen_rocks, key= lambda x : x[1])[1]
            break
    rocks += 1
    rock_shapes.rotate(-1)

print(max(fallen_rocks, key= lambda x : x[1])[1])