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

def optimal_valve_opening_p2(valve_options,time_limit):
    elephant_valve_heap = []
    human_valve_heap = []
    min_cost = 0
    heapq.heappush(human_valve_heap,(0,['AA'],0))
    heapq.heappush(elephant_valve_heap,(0,['AA'],0))
    combined_heap = []
    heapq.heappush(combined_heap,(0,['AA'],0,0))
    while combined_heap:
        valve_info = heapq.heappop(combined_heap)
        time_1 = valve_info[2]
        time_2 = valve_info[3]
        opened_valves = valve_info[1]
        cur_valve_1 = opened_valves[-1] if len(opened_valves) == 1 else opened_valves[-2]
        cur_valve_2 = opened_valves[-1]
        cost = valve_info[0]
        if cost < min_cost:
            min_cost = cost
            print(min_cost)
            print(valve_info)
        # min_cost = min(min_cost,valve_info[0])
        for valve_1 in valve_options:
            if valve_1 not in opened_valves:
                new_time_1 = time_1 + dist_dict[(cur_valve_1,valve_1)]
                cost_1 = (new_time_1 - time_limit) * valve_flows[valve_1]
                for valve_2 in valve_options:
                    if valve_2 != valve_1 and valve_2 not in opened_valves:
                        new_time_2 = time_2 + dist_dict[(cur_valve_2,valve_2)]
                        cost_2 = (new_time_2 - time_limit) * valve_flows[valve_2]
                        if new_time_2 <= time_limit and new_time_1 <= time_limit:
                            new_opened_valves = opened_valves + [valve_1,valve_2]
                            heapq.heappush(combined_heap,(cost_1 + cost_2 + cost,new_opened_valves,new_time_1,new_time_2))
                        elif new_time_2 <= time_limit:
                            new_opened_valves = opened_valves + [valve_2]
                            heapq.heappush(combined_heap,(cost_2 + cost,new_opened_valves,time_1,new_time_2))
                        elif new_time_1 <= time_limit:
                            new_opened_valves = opened_valves + [valve_1]
                            heapq.heappush(combined_heap,(cost_1 + cost,new_opened_valves,new_time_1,time_2))
    return(-min_cost)


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

pressure_released = optimal_valve_opening(pressure_valves,30)
print(pressure_released)

pressure_released_p2 = optimal_valve_opening_p2(pressure_valves,26)
print(pressure_released_p2)


