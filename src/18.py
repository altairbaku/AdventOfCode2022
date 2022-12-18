with open('../input/18.txt') as f:
    lava_cube_coordinates = f.readlines()

lava_set = set()
for coord in lava_cube_coordinates:
    lava_set.add(tuple([int(x) for x in coord.strip().split(',')]))

lava_droplets = list(lava_set)
lava_droplets.sort()
print(lava_droplets)

def get_neighbors(cube_coord):
    neighbors = {(cube_coord[0]+1,cube_coord[1],cube_coord[2]),
    (cube_coord[0]-1,cube_coord[1],cube_coord[2]),
    (cube_coord[0],cube_coord[1]+1,cube_coord[2]),
    (cube_coord[0],cube_coord[1]-1,cube_coord[2]),
    (cube_coord[0],cube_coord[1],cube_coord[2]+1),
    (cube_coord[0],cube_coord[1],cube_coord[2]-1)}
    return neighbors

def interior_check(cube_coord, lava_set):
        surface_x = cube_coord[0]
        surface_y = cube_coord[1]
        surface_z = cube_coord[2]
        back = list(filter(lambda x:x[0] == surface_x and x[1] == surface_y and x[2] < surface_z,lava_set)) == []
        front = list(filter(lambda x:x[0] == surface_x and x[1] == surface_y and x[2] > surface_z,lava_set)) == []
        up = list(filter(lambda x:x[0] == surface_x and x[1] < surface_y and x[2] == surface_z,lava_set)) == []
        down = list(filter(lambda x:x[0] == surface_x and x[1] > surface_y and x[2] == surface_z,lava_set)) == []
        left = list(filter(lambda x:x[0] < surface_x and x[1] == surface_y and x[2] == surface_z,lava_set)) == []
        right = list(filter(lambda x:x[0] > surface_x and x[1] == surface_y and x[2] == surface_z,lava_set)) == []
        return (back or front or up or down or left or right)

exposed_surface_area = 0
exposed_surfaces_p2 = 0
for lava in lava_set:
    neighbors = get_neighbors(lava)
    exposed_surfaces = neighbors ^ (neighbors & lava_set)
    exposed_surface_area += len(exposed_surfaces)
    for exposed_surface in exposed_surfaces:
        # exposed_surfaces_p2 += 1 if interior_check(exposed_surface,lava_set) else 0
        neighbors_2 = get_neighbors(exposed_surface)
        if len(neighbors_2 & lava_set) < 4:
            exposed_surfaces_p2+=1



# air_pockets = 0
# for exposed_surface in exposed_surfaces_set:
#     neighbors = get_neighbors(exposed_surface)
#     air_pockets = neighbors & exposed_surfaces_set
#     air_pockets_2 = neighbors & lava_set
#     print(air_pockets)
#     print(air_pockets_2)

print(exposed_surface_area)
print(exposed_surfaces_p2)

