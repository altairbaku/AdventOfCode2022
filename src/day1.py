with open('../input/day1.txt') as f:
    lines = f.readlines()

d1_input = []
cal_list  = []
sum_cal = 0
for line in lines:
    if line != "\n":
        sum_cal += int(line)
    else:
        cal_list.append(sum_cal)
        sum_cal = 0
cal_list.append(sum_cal)

cal_list.sort(reverse=True)
print("Part 1 : ",cal_list[0])
print("Part 2 : ",sum(cal_list[0:3]))
