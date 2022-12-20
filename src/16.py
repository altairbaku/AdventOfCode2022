import re

with open('../input/16_example.txt') as f:
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

def find_next_node(cur_valve,pressure_released,time,opened_valves,pressure_valves,valve_flows):
    pressure_dict = dict()
    for x in pressure_valves:
        print(opened_valves)
        if x != cur_valve and x not in opened_valves:
            len_path = len(shortest_path(valve_tunnels,cur_valve,x))
            new_time = time - len_path
            if (new_time) > 0:
                new_pressure = pressure_released + (new_time) * valve_flows[x]
                pressure_dict[(cur_valve,x)] = [new_pressure,new_time]
            else:
                return pressure_released,opened_valves
    if pressure_dict:
        max_pressure = max(pressure_dict.values(),key = lambda x:x[0]/(30 - x[1]))
        cur_valve = [k[1] for k,v in pressure_dict.items() if v == max_pressure]
        opened_valves.append(cur_valve)
        time = max_pressure[1]
        pressure_released = max_pressure[0]
        return find_next_node(cur_valve[0],pressure_released,time,opened_valves,pressure_valves,valve_flows)


max_pressure = 0
pressure_valves = [key for (key,value) in valve_flows.items() if value !=0]
cur_valve = 'AA'
time = 30
pressure_released = 0
opened_valves = []
print(find_next_node(cur_valve,pressure_released,time,opened_valves,pressure_valves,valve_flows))
# path_len_dict = dict()
# for x in pressure_valves:
#     len_path = len(shortest_path(valve_tunnels,cur_valve,x))
#     path_len_dict[(cur_valve,x)] = [(time-len_path) * valve_flows[x],time-len_path]
# if path_len_dict:
#     max_pressure = max(path_len_dict.values(),key = lambda x:x[0]/(30 - x[1]))
#     max_valve = [k for k,v in path_len_dict.items() if v == max_pressure]
#     cur_valve = max_valve[0][-1]
#     opened_valves.append(cur_valve)
#     time = max_pressure[1]
#     pressure_released += max_pressure[0]

# while time > 0:
#     for x in pressure_valves:
#         if x != cur_valve and x not in opened_valves:
#             len_path = len(shortest_path(valve_tunnels,cur_valve,x))
#             new_pressure = path_len_dict[max_valve[0]][0] + (time - len_path) * valve_flows[x] if path_len_dict else (time-len_path) * valve_flows[x]
#             valve_list = list(max_valve[0])
#             valve_list.append(x)
#             new_tuple = tuple(valve_list)
#             path_len_dict[new_tuple] = [new_pressure,time-len_path] if (time-len_path) > 0 else [path_len_dict[max_valve[0]][0],0]
#     print(path_len_dict)
#     print(time)
#     if path_len_dict:
#         max_pressure = sorted(path_len_dict.items(),key = lambda x:x[1][0]/(30 - x[1][1]),reverse=True)[:1]
#         path_len_dict = dict(max_pressure)
#         max_valve = [k for k,v in path_len_dict.items() if v == max_pressure]
#         cur_valve = max_valve[0][-1]
#         opened_valves.append(cur_valve)
#         time = max_pressure[1]
#         pressure_released += max_pressure[0]

print(pressure_released)


