import re
with open('../input/19_example.txt') as f:
    blueprints = f.readlines()

for blueprint in blueprints:
    m = re.findall('[0-9]+', blueprint)
    ore_robot_req = int(m[1])
    clay_robot_req = int(m[2])
    obsidian_robot_req = [int(m[3]),int(m[4])]
    geode_robot_req = [int(m[5]),int(m[6])]

    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0

    ore = 0
    clay = 0
    obsidian = 0
    geode = 0

    build_ore = 0
    build_clay = 0
    build_obsidian = 0
    build_geode = 0
    for n in range(0,24):
        ore += ore_robots
        clay += clay_robots
        obsidian += obsidian_robots
        geode += geode_robots

        print(ore)

        if build_ore:
            ore_robots += 1
            build_ore = 0

        if build_clay:
            clay_robots += 1
            build_clay = 0

        if build_obsidian:
            obsidian_robots += 1
            build_obsidian = 0

        if build_geode:
            geode_robots += 1
            build_geode = 0

        if (geode_robot_req[0] <= ore and geode_robot_req[1] <= obsidian):
            ore -= geode_robot_req[0]
            obsidian -= geode_robot_req[1]
            build_geode = 1
        elif (obsidian_robot_req[0] <= ore and obsidian_robot_req[1] <= clay):
            ore -= obsidian_robot_req[0]
            clay -= obsidian_robot_req[1]
            build_obsidian = 1
        elif (clay_robot_req <= ore):
            ore -= clay_robot_req
            build_clay = 1
        elif (ore_robot_req <= ore):
            ore -= ore_robot_req
            build_ore = 1
    print(geode)

