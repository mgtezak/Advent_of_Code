path = 'Advent_of_Code/2018/puzzle_input/06.txt'

with open(path) as input:
    coords = [tuple(map(int, line.split(', '))) for line in input.read().split('\n')]

'''
If the area around a pair of coordinates touches the frame of the grid, then it's infinite. 
The frame is defined by the values x_min, x_max, y_min and y_max.
'''

x_vals = sorted(x for x, _ in coords)
y_vals = sorted(y for _, y in coords)
x_min, x_max = x_vals[0], x_vals[-1]
y_min, y_max = y_vals[0], y_vals[-1]


areas = {(x, y): 0 for x, y in coords}   # part 1
proximity_region = []                    # part 2


def get_nearest_coord(x, y):
    distances = {(v, w): abs(x-v) + abs(y-w) for v, w in coords}
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    if sum(distances.values()) < 10_000:   # part 2
        proximity_region.append(1)
    if sorted_distances[0][1] == sorted_distances[1][1]:
        return None
    return sorted_distances[0][0]


for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        nearest = get_nearest_coord(x, y)
        if nearest in areas:
            if x in (x_min, x_max) or y in (y_min, y_max):
                del areas[nearest]
            else:
                areas[nearest] += 1


print(f'Part 1: {max(areas.values())}')
print(f'Part 2: {sum(proximity_region)}')