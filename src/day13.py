from functools import cmp_to_key

with open('../input/day13.txt') as f:
    packets = f.readlines()

def split_packet(packet):
    index = 1
    bracket_count = 0
    split_packet = []
    cur_item = ''
    while index != len(packet)-1:
        cur_char = packet[index]
        next_char = packet[index+1]
        if cur_char == '[':
            bracket_count += 1
        elif cur_char == ']':
            bracket_count -= 1
        if cur_char not in ['[',']',','] and next_char not in ['[',']',',']:
            cur_item = cur_item + cur_char + next_char
            index += 2
        else:
            cur_item = cur_item + cur_char
            index += 1
        if bracket_count == 0 and cur_item != ',':
            if cur_item[0] == ',':
                split_packet.append(cur_item[1:])
            else:
                split_packet.append(cur_item)
            cur_item = ''
    return split_packet

def compare_packets(left,right):
    left_smaller = 0
    if (type(left) == list and len(left) == 0 and len(right) != 0):
        left_smaller = -1
    for n in range(len(left)):
        if (type(right) == list and len(right) == 0) or len(right) == n:
            left_smaller = 1
            break
        left_item = left[n][0] if type(left) == list else left
        right_item = right[n][0] if type(right) == list else right
        if left_item == '[' and right_item == '[':
            new_left = split_packet(left[n])
            new_right = split_packet(right[n])
            left_smaller = compare_packets(new_left,new_right)
        elif left_item != '[' and right_item != '[':
            left_int = int(left[n]) if type(left) == list else int(left)
            right_int = int(right[n]) if type(right) == list else int(right)
            if left_int < right_int:
                left_smaller = -1
            elif right_int < left_int:
                left_smaller = 1
        elif left_item == '[' and right_item != '[':
            left_smaller = compare_packets(split_packet(left[n]),right[n])
        else:
            left_smaller = compare_packets(left[n],split_packet(right[n]))
        if left_smaller != 0:
            return left_smaller
    return -1 if len(left) < len(right) else left_smaller

index_sum = 0
for n in range(0,len(packets),3):
    left = split_packet(packets[n].strip())
    right = split_packet(packets[n+1].strip())
    right_order = compare_packets(left,right)
    if  right_order == -1:
        index_sum += (n/3 + 1)

print(index_sum)

def compare(i1,i2):
    return compare_packets(split_packet(i1),split_packet(i2))

packets_without_spaces = []
for packet in packets:
    if packet != '\n':
        packets_without_spaces.append(packet.strip())

packets_without_spaces.extend(['[[2]]','[[6]]'])
# swapped = 1
# while swapped != 0:
#     index = 0
#     swapped = 0
#     for i in range(0,len(packets_without_spaces)-1):
#         for j in range(i+1,len(packets_without_spaces)):
#             first = split_packet(packets_without_spaces[i])
#             second = split_packet(packets_without_spaces[j])
#             if(compare_packets(first,second) == 0):
#                 temp = packets_without_spaces[i]
#                 packets_without_spaces[i] = packets_without_spaces[j]
#                 packets_without_spaces[j] = temp
#                 swapped = 1

# packets_without_spaces.sort(key = compare_packets)
new_list = sorted(packets_without_spaces,key=cmp_to_key(compare))
new_list_2 = sorted(new_list,key = cmp_to_key(compare))
print((new_list_2.index('[[2]]') + 1) * (new_list_2.index('[[6]]') + 1))
# for item in new_list:
#     print(item)
    



