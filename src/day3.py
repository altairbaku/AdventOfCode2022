import string
with open('../input/day3.txt') as f:
    rucksacks = f.readlines()

dict = {}
keys = string.ascii_letters
n = 1
for x in keys:
    dict[x] = n
    n+=1

sum_p1 = 0
for rucksack in rucksacks:
    n_half  = int(len(rucksack)/2)
    compartment_1 = set(rucksack[0:n_half])
    compartment_2 = set(rucksack[n_half:])
    for item in compartment_1:
        if item in compartment_2:
            sum_p1 += dict[item]
            break

sum_p2 = 0
for n in range(0,len(rucksacks),3):
    for item in set(rucksacks[n]):
        if item in set(rucksacks[n+1].strip()) and item in set(rucksacks[n+2].strip()):
            sum_p2+=dict[item]

print("Part 1 : ",sum_p1)
print("Part 2 : ",sum_p2)

