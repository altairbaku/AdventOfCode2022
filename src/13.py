from functools import cmp_to_key
import ast

with open('../input/13.txt') as f:
    packets = f.readlines()

def compare_packets(left,right):
    retval = 0
    if type(left) is list and type(right) is list:
        for n in range(len(left)):
            retval =  1 if len(right) == n else compare_packets(left[n],right[n])
            if retval != 0:
                return retval
        if len(left) < len(right):
            retval = -1
        elif len(left) > len(right):
            retval = 1
        else:
            retval = 0
    elif type(left) is int and type(right) is int:
        if left < right:
            retval = -1
        elif right < left:
            retval = 1
    elif type(right) is int:
        retval = compare_packets(left,[right])
    else:
        retval = compare_packets([left],right)
    return retval

index_sum = 0
for n in range(0,len(packets),3):
    left = ast.literal_eval(packets[n].strip())
    right = ast.literal_eval(packets[n+1].strip())
    out = compare_packets(left,right)
    if (out == -1 or out == 0):
        index_sum += int(n/3+1)

print("Part 1 : ",index_sum)

packets_without_spaces = []
packets.extend(['[[2]]','[[6]]'])
for packet in packets:
    if packet != '\n':
        packets_without_spaces.append(ast.literal_eval(packet.strip()))

new_list = sorted(packets_without_spaces, key = cmp_to_key(compare_packets))
print("Part 2 : ",(new_list.index([[2]]) + 1) * (new_list.index([[6]]) + 1))



