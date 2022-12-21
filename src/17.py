with open('../input/17.txt') as f:
    lines = f.readlines()

for line in lines:
    jet_pattern = [x for x in line.strip()]

minus = set((2,3),(3,3),(4,3),(5,3))
rocks = 0
while rocks < 2022:
    rocks += 1