import re
import math
from copy import deepcopy

with open('../input/19.txt') as f:
    blueprints = f.readlines()

bps = []
for blueprint in blueprints:
    m = re.findall('[0-9]+', blueprint)
    ore_robot_req = [int(m[1]),0,0,0]
    clay_robot_req = [int(m[2]),0,0,0]
    obsidian_robot_req = [int(m[3]),int(m[4]),0,0]
    geode_robot_req = [int(m[5]),0,int(m[6]),0]
    bps.append([ore_robot_req,clay_robot_req,obsidian_robot_req,geode_robot_req])

def find_max_geodes(req,timemax):
    time = 0
    robots = [1,0,0,0]
    resources = [0,0,0,0]
    mineral_heap = []
    mineral_heap.append([time, robots, resources])
    max_geodes = 0

    max_res = 4 * [0]
    for cost in req:
        for j in range(len(cost)):
            if cost[j] > max_res[j]:
                max_res[j] = cost[j]

    while mineral_heap:
        time, robots, resources = mineral_heap.pop(0)
        geodes = resources[3] + robots[3] * (timemax - time)
        if geodes > max_geodes:
            max_geodes = geodes

        for i in range(len(req)):
            cost = req[i]
            time_needed = [0,0,0,0]
            for j in range(len(cost)):
                if cost[j]:
                    if cost[j] <= resources[j]:
                        continue
                    else:
                        if robots[j]:
                            time_needed[j] = math.ceil((cost[j] - resources[j])/robots[j])
                        else:
                            time_needed[j] = timemax + 1

            dt = max(time_needed)
            if time+dt+1+1 <= timemax:
                resources_new = 4 * [0]
                for n in range(4):
                    resources_new[n] = resources[n] + (dt+1) * robots[n] - cost[n]

                robots_new = deepcopy(robots)
                robots_new[i] += 1

                if sum([robots_new[x] <=  max_res[x] for x in range(3)]) != 3:
                    continue

                timeleft = timemax - (time+dt+1)
                geodes_new_ideal = (timeleft - 1)*timeleft//2
                geodes_final_ideal = resources_new[3] + timeleft * robots_new[3] + geodes_new_ideal
                if geodes_final_ideal <= max_geodes:
                    continue
                
                state_new = [time+dt+1,robots_new,resources_new]
                if state_new not in mineral_heap:
                    mineral_heap.append(state_new)
    return max_geodes


id = 1
quality_sum = 0
for bp in bps:
    quality_sum += id * find_max_geodes(bp,24)
    id+=1
print(quality_sum)

quality_prod = 1
for n in range(3):
    bp_geode = find_max_geodes(bps[n],32)
    quality_prod *= bp_geode
print(quality_prod)

    
