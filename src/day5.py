import re
from collections import defaultdict
  
with open('../input/day5_example.txt') as f:
    lines = f.readlines()

crate_dict = defaultdict(list)

while lines[0] != "\n":
    container_regex = re.compile("[[]([A-Z])[]]")
    matches = container_regex.finditer(lines[0])
    lines.remove(lines[0])
    for hit in matches:
        crate_dict[int(hit.start()/4) + 1].append(hit.group()[1])

print(crate_dict)

for line in lines[1::]:
    instructions = [int(s) for s in line.split() if s.isdigit()]
    crate_dict[instructions[2]] = crate_dict[instructions[1]][0:instructions[0]] + crate_dict[instructions[2]]
    del crate_dict[instructions[1]][0:instructions[0]]
    print(crate_dict)

for n in range(len(crate_dict)):
    print(crate_dict[n+1][0])

        




