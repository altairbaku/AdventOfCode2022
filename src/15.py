import re

def manhattan_distance(a,b):
    dist = abs(a[0]-b[0])+abs(a[1]-b[1])
    return dist

with open('../input/15.txt') as f:
    sensor_readings = f.readlines()

sensors = dict()
for reading in sensor_readings:
    m = re.search(r'Sensor at x=(\d+|-\d+), y=(\d+|-\d+): closest beacon is at x=(\d+|-\d+), y=(\d+|-\d+)',reading)
    sensor = (int(m.group(1)),int(m.group(2)))
    beacon = (int(m.group(3)),int(m.group(4)))
    sensors[sensor] = manhattan_distance(sensor,beacon)

y = 2000000
x_min = 0
x_max = 0
for sensor in sensors:
    x_pos = sensors[sensor] - abs(sensor[1]-y)
    if x_pos >= 0:
        x_left = sensor[0] - x_pos
        x_right = sensor[0] + x_pos
        x_min = min(x_min,x_left)
        x_max = max(x_max,x_right)

print("Part 1 : ",x_max-x_min)

bound = 4000000
for y in range(0,bound+1):
    no_beacons = []
    for sensor in sensors:
        x_pos = sensors[sensor] - abs(sensor[1]-y)
        if x_pos >= 0:
            x_1 = sensor[0] - x_pos
            x_2 = sensor[0] + x_pos
            x_left = max(0,min(x_1,x_2))
            x_right  = min(bound,max(x_1,x_2))
            no_beacons.append((x_left,x_right))
    no_beacons.sort()
    x_max = 0
    x_min = bound
    for x in no_beacons:
        if x[0] <= x_max and x[1] > x_max:
            x_max = x[1]
        if x[0] <= x_min:
            x_min = x[0]
    if (x_max-x_min) < bound:
        print("Part 2 : ", 4000000 * (x_max+1) + y)
        break
    


    

    

