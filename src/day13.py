with open('../input/day13.txt') as f:
    packets = f.readlines()

for n in range(0,len(packets),3):
    left = packets[n].strip().split(',')
    right = packets[n+1].strip().split(',')