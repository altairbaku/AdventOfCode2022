import re
from itertools import combinations
import heapq

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

def optimal_valve_opening(valve_options,time_limit):
    valve_heap = []
    heapq.heappush(valve_heap,(0,['AA'],0))
    min_cost = 0
    while valve_heap:
        valve_info = heapq.heappop(valve_heap)
        opened_valves = valve_info[1]
        cur_valve = opened_valves[-1]
        time = valve_info[2]
        min_cost = min(min_cost,valve_info[0])
        for valve in valve_options:
            if valve not in opened_valves:
                new_time = time + dist_dict[(cur_valve,valve)]
                cost = valve_info[0] + (new_time - time_limit) * valve_flows[valve]
                new_opened_valves = opened_valves + [valve]
                if new_time <= time_limit:
                    heapq.heappush(valve_heap,(cost,new_opened_valves,new_time))
    return (-min_cost)

pressure_valves = [key for (key,value) in valve_flows.items() if value !=0]
valve_combinations = combinations(pressure_valves,2)
dist_dict = dict()
start_valve = 'AA'
for combo in valve_combinations:
    combo_dist = len(shortest_path(valve_tunnels,combo[0],combo[1]))
    dist_dict[combo] = combo_dist
    dist_dict[(combo[1],combo[0])] = combo_dist
    dist_dict[(start_valve,combo[0])] = len(shortest_path(valve_tunnels,start_valve,combo[0]))
    dist_dict[(start_valve,combo[1])] = len(shortest_path(valve_tunnels,start_valve,combo[1]))

pressure_released = optimal_valve_opening(pressure_valves,30)
print("Part 1 : ",pressure_released)

human_valve_combos = combinations(pressure_valves,int(len(pressure_valves)/2))
max_pressure = 0
for human_valves in human_valve_combos:
    human_pressure = optimal_valve_opening(human_valves,26)
    elephant_valves = [x for x in pressure_valves if x not in human_valves]
    elephant_pressure = optimal_valve_opening(elephant_valves,26)
    max_pressure = max(max_pressure,human_pressure + elephant_pressure)

print("Part 2 : ",max_pressure)


