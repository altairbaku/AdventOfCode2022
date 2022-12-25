from collections import deque,defaultdict
with open('../input/23.txt') as f:
    lines = f.readlines()

elf_number = 0
elf_pos_dict = dict()
elf_pos_set = set()
for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        if lines[i][j] == '#':
            elf_pos_dict[elf_number] = (i,j)
            elf_number += 1
            elf_pos_set.add((i,j))

directional_elves = deque([lambda x: [(x[0]-1,x[1]-1),(x[0]-1,x[1]),(x[0]-1,x[1]+1)],
                            lambda y: [(y[0]+1,y[1]-1),(y[0]+1,y[1]),(y[0]+1,y[1]+1)],
                            lambda z: [(z[0]-1,z[1]-1),(z[0],z[1]-1),(z[0]+1,z[1]-1)],
                            lambda w: [(w[0]-1,w[1]+1),(w[0],w[1]+1),(w[0]+1,w[1]+1)]])

all_directions = lambda a: [(a[0]-1,a[1]-1),(a[0]-1,a[1]),(a[0]-1,a[1]+1),(a[0]+1,a[1]-1),(a[0]+1,a[1]),(a[0]+1,a[1]+1),(a[0],a[1]+1),(a[0],a[1]-1)]

for round in range(1000):
    d = defaultdict(list)
    for elf,pos in elf_pos_dict.items():
        neighbors = all_directions(pos)
        neighbors_set = set(neighbors)
        if neighbors_set.intersection(elf_pos_set):
            for direction in directional_elves:
                new_pos = direction(pos)
                new_pos_set = set(new_pos)
                if not new_pos_set.intersection(elf_pos_set):
                    d[new_pos[1]].append(elf)
                    break

    moving_elves = dict(filter(lambda elem : len(elem[1]) == 1,d.items()))
    for k,v in moving_elves.items():
        elf_pos_set.remove(elf_pos_dict[v[0]])
        elf_pos_dict[v[0]] = k
        elf_pos_set.add(k)
    directional_elves.rotate(-1)
    if round == 9:
        p1 = (max(elf_pos_set,key = lambda x:x[0])[0] - min(elf_pos_set,key = lambda x:x[0])[0] + 1) * (max(elf_pos_set,key = lambda x:x[1])[1] - min(elf_pos_set,key = lambda x:x[1])[1] + 1) - len(elf_pos_set)
        print("Part 1 : ",p1)
    if not moving_elves:
        print("Part 2 : ",round + 1)
        break




