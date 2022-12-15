import re

with open('../input/day15.txt') as f:
    sensor_readings = f.readlines()

for reading in sensor_readings:
    m = re.search(r'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)',reading)
    print(reading)
    print(m.group(2))

    

