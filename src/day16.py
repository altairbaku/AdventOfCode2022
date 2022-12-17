import re

with open('../input/day16.txt') as f:
    valve_scan = f.readlines()

valve_flows = dict()
valve_tunnels = dict()
for scan in valve_scan:
    split_scan = scan.split(";")
    valve_info = re.search(r'Valve ([A-Z]+) has flow rate=(\d+)',split_scan[0])
    cur_valve = valve_info.group(1)
    valve_flows[cur_valve] = int(valve_info.group(2))
    valve_tunnels[cur_valve] = re.findall(r'([A-Z]+)',split_scan[1])

valves_opened = []


