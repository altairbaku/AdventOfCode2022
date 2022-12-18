with open('../input/04.txt') as f:
    pairs = f.readlines()

subset_count = 0
overlap_count = 0
for pair in pairs:
    sections = pair.split(",")
    section_range_1 = list(map(int,sections[0].split("-")))
    section_range_2 = list(map(int,sections[1].split("-")))
    if (section_range_1[0] >= section_range_2[0] and section_range_1[1] <= section_range_2[1]) or (section_range_1[0] <= section_range_2[0] and section_range_1[1] >= section_range_2[1]):
        subset_count += 1
    if (section_range_1[0] <= section_range_2[1] and section_range_1[0] >= section_range_2[0]) or (section_range_2[0] <= section_range_1[1] and section_range_2[0] >= section_range_1[0]):
        overlap_count +=1
    
print("Part 1 : ",subset_count)
print("Part 2 : ",overlap_count)
    
