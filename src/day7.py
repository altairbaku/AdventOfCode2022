with open('../input/day7.txt') as f:
    lines = f.readlines()

def directory_size_list(filesystem,index):
    directory_size = 0
    p1_sol = 0
    filesystem_len = len(filesystem)
    while index != filesystem_len:
        line = filesystem[index]
        index += 1
        if line[2:4] == "cd" and line[5:] != "..\n":
            sub_directory_size,p1_sub_size,index = directory_size_list(filesystem,index)
            directory_size += sub_directory_size
            p1_sol += p1_sub_size
        elif line[2:4] == "cd" and line[5:] == "..\n":
            if directory_size <= 100000:
                p1_sol += directory_size
            print(directory_size)
            return directory_size,p1_sol,index
        elif line[0:3] != "dir" and line[2:4] != "ls":
            directory_size += int(line.split()[0])
    
    print(directory_size)
    if directory_size <= 100000:
        p1_sol += directory_size
    return directory_size,p1_sol,index

total_size,p1_size,index = directory_size_list(lines,0)

print(total_size)
print(p1_size)

