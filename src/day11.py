from collections import deque
import math
from copy import deepcopy

with open('../input/day11.txt') as f:
    lines = f.readlines()

monkey_count = 0
items = list(deque())
operations = list()
tests = list()
temp_q = deque()
throws = list()
temp_throws = []
for line in lines:
    if line == "\n":
        throws.append(temp_throws)
        monkey_count += 1
        temp_q = deque()
        temp_throws = []
    else:
        line_els = line.strip().split(':')
        if line_els[0] == 'Starting items':
            st_items = line_els[1].strip().split(', ')
            for n in range(len(st_items)):
                temp_q.append(int(st_items[n]))
            items.append(temp_q)
        elif line_els[0] == 'Operation':
            operations.append(line_els[1].strip().split('=')[1].strip())
        elif line_els[0] == 'Test':
            tests.append(int(line_els[1].split()[-1]))
        elif line_els[0] == 'If true' or line_els[0] == 'If false':
            temp_throws.append(int(line_els[1].split()[-1]))
throws.append(temp_throws)
monkey_count += 1

def p1(items,operations,tests,throws):
    inspection_count =  [0] * monkey_count
    for _ in range(20):
        for i in range(monkey_count):
            while items[i]:
                inspection_count[i] += 1
                old = items[i].popleft()
                new = int(eval(operations[i])/3)
                rem = new % tests[i]
                if rem == 0:
                    items[throws[i][0]].append(new)
                else:
                    items[ throws[i][1]].append(new)
    inspection_count.sort()
    return (inspection_count[-1] * inspection_count[-2])


def p2(items,operations,tests,throws):
    inspection_count =  [0] * monkey_count
    for _ in range(10000):
        for i in range(monkey_count):
            while items[i]:
                inspection_count[i] += 1
                old = items[i].popleft()
                new = int(eval(operations[i]))
                rem = new % tests[i]
                new = new % math.prod(tests)
                if rem == 0:
                    items[throws[i][0]].append(new)
                else:
                    items[ throws[i][1]].append(new)
    inspection_count.sort()
    return (inspection_count[-1] * inspection_count[-2])

print("Part 1 : ", p1(deepcopy(items),operations,tests,throws))
print("Part 2 : ", p2(deepcopy(items),operations,tests,throws))