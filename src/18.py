from collections import deque
with open('../input/18.txt') as f:
    lava_cube_coordinates = f.readlines()

lava_set = set()
for coord in lava_cube_coordinates:
    lava_set.add(tuple([int(x) for x in coord.strip().split(',')]))

lava_droplets = list(lava_set)
lava_droplets.sort()
x_max = max(lava_droplets,key = lambda x: x[0])[0] + 1
x_min = min(lava_droplets,key = lambda x: x[0])[0] - 1
y_max = max(lava_droplets,key = lambda x: x[1])[1] + 1
y_min = min(lava_droplets,key = lambda x: x[1])[1] - 1
z_max = max(lava_droplets,key = lambda x: x[2])[2] + 1
z_min = min(lava_droplets,key = lambda x: x[2])[2] - 1


def get_neighbors(cube_coord):
    x = cube_coord[0]
    y = cube_coord[1]
    z = cube_coord[2]
    if x > x_min and x < x_max and y > y_min and y < y_max and z > z_min and z < z_max:
        neighbors = {(x+1,y,z),
        (x-1,y,z),
        (x,y+1,z),
        (x,y-1,z),
        (x,y,z+1),
        (x,y,z-1)}
    else:
        neighbors = set()
    return neighbors

def flood_fill(cube_coord, lava_set, air_pockets):
    visited = set()
    to_visit = deque([cube_coord])
    while to_visit:
        current_coord = to_visit.popleft()
        neighbors = get_neighbors(current_coord)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in lava_set and neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        else:
            return 1,air_pockets
        visited.add(current_coord)
    new_set = air_pockets.union(visited)
    return 0,new_set

exposed_surface_area = 0
exposed_surfaces_p2 = 0
air_pockets = set()
for lava in lava_set:
    neighbors = get_neighbors(lava)
    exposed_surfaces = neighbors ^ (neighbors & lava_set)
    exposed_surface_area += len(exposed_surfaces)
    for exposed_surface in exposed_surfaces:
        if exposed_surface not in air_pockets:
            exterior,air_pockets = flood_fill(exposed_surface,lava_set,air_pockets)
            exposed_surfaces_p2 += exterior

print("Part 1 : ",exposed_surface_area)
print("Part 2 : ",exposed_surfaces_p2)

