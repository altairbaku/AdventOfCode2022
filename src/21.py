with open('../input/21.txt') as f:
    lines = f.readlines()

monkey_yells = dict()
for line in lines:
    split_line = line.strip().split(': ')
    monkey_yells[split_line[0]] = split_line[1]

def eval_monkey(yells_dict,monkey):
    print(monkey)
    try:
        yell = eval(yells_dict[monkey])
    except:
        split_equation = yells_dict[monkey].split()
        print(split_equation)
        yells_dict[monkey] = yells_dict[monkey].replace(split_equation[0],str(eval_monkey(yells_dict, split_equation[0])))
        yells_dict[monkey] = yells_dict[monkey].replace(split_equation[2],str(eval_monkey(yells_dict, split_equation[2])))
        yell = int(eval(yells_dict[monkey]))
    return yell

p1 = eval_monkey(monkey_yells,'root')
print(p1)
