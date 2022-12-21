from copy import deepcopy
with open('../input/21.txt') as f:
    lines = f.readlines()

monkey_yells = dict()
for line in lines:
    split_line = line.strip().split(': ')
    monkey_yells[split_line[0]] = split_line[1]

def eval_monkey(yells_dict,monkey):
    try:
        yell = int(eval(yells_dict[monkey]))
    except:
        split_equation = yells_dict[monkey].split()
        yells_dict[monkey] = yells_dict[monkey].replace(split_equation[0],str(eval_monkey(yells_dict, split_equation[0])))
        yells_dict[monkey] = yells_dict[monkey].replace(split_equation[2],str(eval_monkey(yells_dict, split_equation[2])))
        yell = int(eval(yells_dict[monkey]))
    return yell

# def update_equation(eq):
#     eq_new = []
#     eq_new.append('humn')
#     left = eq[0]
#     right = eq[1].split()
#     if right[1] == '+':
#         eq_new.append()

monkey_yells_p1 = deepcopy(monkey_yells)
p1 = eval_monkey(monkey_yells_p1,'root')
print(p1)
components = monkey_yells_p1['root'].split()
print(list(filter(lambda elem: 'humn' in elem[1], monkey_yells.items())))

split_root = monkey_yells['root'].split()
monkey_yells['root'] = monkey_yells['root'].replace(split_root[1],'-')

monkey_yells['humn'] = 'lpjj + pvrr'
humn_value = 3887609739999
while True:
    temp_monkey_yells = deepcopy(monkey_yells)
    temp_monkey_yells['humn'] = str(humn_value)
    root_yell = eval_monkey(temp_monkey_yells,'root')
    if root_yell == 0:
        print(humn_value)
        break
    else:
        humn_value += 1

