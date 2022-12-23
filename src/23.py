with open('../input/23.txt') as f:
    lines = f.readlines()

elf_number = 0
elf_pos_dict = dict()
for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        print(lines[i][j])
        if lines[i][j] == '#':
            elf_pos_dict[elf_number] = [i,j]
            elf_number += 1

print(elf_pos_dict)