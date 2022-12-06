import re
from collections import defaultdict
import copy
  
with open('../input/day5.txt') as f:
    lines = f.readlines()

crate_dict_p1 = defaultdict(list)

while lines[0] != "\n":
    container_regex = re.compile("[[]([A-Z])[]]")
    matches = container_regex.finditer(lines[0])
    lines.remove(lines[0])
    for hit in matches:
        crate_dict_p1[int(hit.start()/4) + 1].append(hit.group()[1])

crate_dict_p2 = copy.deepcopy(crate_dict_p1)

for line in lines[1::]:
    instructions = [int(s) for s in line.split() if s.isdigit()]
    stack = crate_dict_p1[instructions[1]][0:instructions[0]]
    stack.reverse()
    crate_dict_p1[instructions[2]] = stack + crate_dict_p1[instructions[2]]
    del crate_dict_p1[instructions[1]][0:instructions[0]]
    crate_dict_p2[instructions[2]] = crate_dict_p2[instructions[1]][0:instructions[0]] + crate_dict_p2[instructions[2]]
    del crate_dict_p2[instructions[1]][0:instructions[0]]

p1 = ''
p2 = ''

for n in range(len(crate_dict_p1)):
    p1 += crate_dict_p1[n+1][0]
    p2 += crate_dict_p2[n+1][0]

print("Part 1 : ",p1)
print("Part 2 : ",p2)



        




