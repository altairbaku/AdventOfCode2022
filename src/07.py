with open('../input/07.txt') as f:
    lines = f.readlines()

def directory_size_list(filesystem,index):
    directory_size = 0
    directory_sizes = []
    filesystem_len = len(filesystem)
    while index != filesystem_len:
        line = filesystem[index]
        index += 1
        if line[2:4] == "cd" and line[5:] != "..\n":
            index,sub_size_list,sub_size = directory_size_list(filesystem,index)
            directory_sizes.extend(sub_size_list)
            directory_size += sub_size
        elif line[2:4] == "cd" and line[5:] == "..\n":
            directory_sizes.append(directory_size)
            return index,directory_sizes,directory_size
        elif line[0:3] != "dir" and line[2:4] != "ls":
            directory_size += int(line.split()[0])
    
    directory_sizes.append(directory_size)
    return index,directory_sizes,directory_size

index,size_list,total_size = directory_size_list(lines,0)

p1_list = filter(lambda x: x <= 100000,size_list)
p2_list = filter(lambda y: y >= max(size_list)-40000000,size_list)
print(sum(p1_list))
print(sorted(p2_list)[0])

