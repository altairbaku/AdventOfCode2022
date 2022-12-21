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

def find_next_valve(pressure_valves,opened_valves,cur_valve):
    pressure_max = -10
    if len(pressure_valves) -len(opened_valves) > 1:
        for x in pressure_valves:
            pressure = 0
            for y in pressure_valves:
                if x not in opened_valves and y not in opened_valves and x != y:
                    pressure += (30 - len(shortest_path(valve_tunnels,x,y))) * valve_flows[y]
            print(x,pressure)
            pressure = pressure * (30 - len(shortest_path(valve_tunnels,x,cur_valve))) * valve_flows[x]
            print(x,pressure)
            if pressure > pressure_max:
                pressure_max = pressure
                next_valve = x
            elif pressure == pressure_max:
                next_valve = x if valve_flows[x] > valve_flows[next_valve] else next_valve
    else:
        rem_valves = [x for x in pressure_valves if x not in set(opened_valves)]
        next_valve = rem_valves[0]
    return len(shortest_path(valve_tunnels,cur_valve,next_valve)),next_valve

pressure_released = 0
pressure_valves = [key for (key,value) in valve_flows.items() if value !=0]
pressure_valves = sorted(pressure_valves,key = lambda x:valve_flows[x],reverse=True)
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
        print(opened_valves)

print(pressure_released)



