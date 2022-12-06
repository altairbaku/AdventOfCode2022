with open('../input/day6.txt') as f:
    lines = f.readlines()

def packet_start_marker(input,distinct_len):
    for n in range(distinct_len,len(input)):
        if len(set(input[n-distinct_len:n])) == distinct_len:
            return n

print("Part 1 : ",packet_start_marker(lines[0],4))
print("Part 2 : ",packet_start_marker(lines[0],14))