import string
with open('../input/day3.txt') as f:
    rucksacks = f.readlines()

dict = {}
keys = string.ascii_letters
n = 1
for x in keys:
    dict[x] = n
    n+=1

sum_items = 0
for rucksack in rucksacks:
    n_half  = int(len(rucksack)/2)
    compartment_1 = set(rucksack[1:n_half])
    compartment_2 = set(rucksack[n_half::])
    for item in compartment_1:
        if item in compartment_2:
            print(item,dict[item])
            sum_items += dict[item]
            break

print(sum_items)

