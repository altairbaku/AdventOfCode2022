import re
from itertools import combinations, permutations

with open('../input/16.txt') as f:
    valve_scan = f.readlines()

valve_flows = dict()
valve_tunnels = dict()
for scan in valve_scan:
    split_scan = scan.split(";")
    valve_info = re.search(r'Valve ([A-Z]+) has flow rate=(\d+)',split_scan[0])
    cur_valve = valve_info.group(1)
    valve_flows[cur_valve] = int(valve_info.group(2))
    valve_tunnels[cur_valve] = re.findall(r'([A-Z]+)',split_scan[1])

def shortest_path(graph,initial,end):
    path_list = [[initial]]
    path_index = 0
    visited = {initial}
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]

        if end in next_nodes:
            current_path.append(end)
            return current_path

        for next_node in next_nodes:
            if not next_node in visited:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                visited.add(next_node)
        path_index += 1
    return []

pressure_valves = [key for (key,value) in valve_flows.items() if value !=0]
valve_combinations = list(combinations(pressure_valves,2))
dist_dict = dict()
start_valve = 'AA'
for combo in valve_combinations:
    combo_dist = len(shortest_path(valve_tunnels,combo[0],combo[1]))
    dist_dict[combo] = combo_dist
    dist_dict[(combo[1],combo[0])] = combo_dist
    dist_dict[(start_valve,combo[0])] = len(shortest_path(valve_tunnels,start_valve,combo[0]))
    dist_dict[(start_valve,combo[1])] = len(shortest_path(valve_tunnels,start_valve,combo[1]))


def find_next_valve(pressure_valves,opened_valves,cur_valve):
    max_cost = -10
    unopened_valves = [x for x in pressure_valves if x not in opened_valves]
    permute_valves = list(permutations(unopened_valves,2))
    if (permute_valves):
        for valve_combo in permute_valves:
            flow_0 = valve_flows[valve_combo[0]]
            flow_1 = valve_flows[valve_combo[1]]
            dist_0 = 30 - dist_dict[(cur_valve,valve_combo[0])]
            dist_1 = dist_0 - dist_dict[valve_combo]
            cost = (flow_0 * dist_0 + flow_1 * dist_1)/(30 - dist_1)
            if cost > max_cost:
                max_cost = cost
                time = 30 - dist_0
                next_valve = valve_combo[0]
    else:
        time = dist_dict[cur_valve,unopened_valves[0]]
        next_valve = unopened_valves[0]
    return time,next_valve

pressure_released = 0
time = 30
cur_valve = 'AA'
opened_valves = []
while True:
    if time <= 0 or len(pressure_valves) == len(opened_valves):
        break
    time_elapsed,next_valve = find_next_valve(pressure_valves,opened_valves,cur_valve)
    time -= time_elapsed
    if time > 0:
        pressure_released += time * valve_flows[next_valve]
        cur_valve = next_valve
        opened_valves.append(cur_valve)

print(pressure_released)



