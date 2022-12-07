with open('../input/day7.txt') as f:
    lines = f.readlines()

size_dict = dict()
subfolder_dict = dict()
cur_dir = '/'
for line in lines:
    if line[2:4] == "cd":
        if line[5:] != "..\n":
            prev_dir = cur_dir
            cur_dir = line[5:].strip()
        else:
            cur_dir = prev_dir
    elif line[0:3] == "dir":
        if cur_dir not in subfolder_dict:
            subfolder_dict[cur_dir] = [line[4:].strip()]
        else:
            subfolder_dict[cur_dir].append(line[4:].strip())
    elif line[2:4] != "ls":
        size = int(line.split()[0])
        if cur_dir not in size_dict:
            size_dict[cur_dir] = size
        else:
            size_dict[cur_dir] += size

def total_size(size_dict,subfolder_dict,key):
    if key in subfolder_dict:
        for value in subfolder_dict[key]:
            size_dict[key] += total_size(size_dict,subfolder_dict,value)
    else:
        return size_dict[key]
    return size_dict[key]

total_size(size_dict,subfolder_dict,'/')

p1 = [x if x <= 100000 else 0 for x in size_dict.values()]
print(sum(p1))

