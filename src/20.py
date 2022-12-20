from copy import deepcopy
from collections import deque

with open('../input/20.txt') as f:
    lines = f.readlines()
file_p1 = deque([(int(value.strip()),index) for index,value in enumerate(lines)])

def move(file,position):
    index = file.index(position)
    file.rotate(-index)
    elem = file.popleft()
    file.rotate(-position[0])
    file.append(elem)
    return file

mixed_file = deepcopy(file_p1)

for position in file_p1:
    mixed_file = move(mixed_file,position)

mixed_file.rotate(-mixed_file.index((0,4094)))
print("Part 1 : ",mixed_file[1000][0]+mixed_file[2000][0]+mixed_file[3000][0])

decryption_key = 811589153
file_p2 = deque([(int(value.strip()) * decryption_key,index) for index,value in enumerate(lines)])
mixed_file_p2 = deepcopy(file_p2)

for _ in range(10):
    for position in file_p2:
        mixed_file_p2 = move(mixed_file_p2,position)

mixed_file_p2.rotate(-mixed_file_p2.index((0,4094)))
print("Part 2 : ",mixed_file_p2[1000][0]+mixed_file_p2[2000][0]+mixed_file_p2[3000][0])
