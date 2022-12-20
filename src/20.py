from copy import deepcopy
with open('../input/20_example.txt') as f:
    lines = f.readlines()
    

initial_file = [int(line.strip()) for line in lines]

mixed_file = deepcopy(initial_file)
for position in initial_file:
    index = mixed_file.index(position)
    new_index = (index + position) % len(initial_file)
    mixed_file.remove(position)
    mixed_file = mixed_file[:new_index] + [position] + mixed_file[new_index:]
    print(mixed_file)

print(mixed_file)