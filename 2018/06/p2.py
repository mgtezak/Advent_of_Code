def part2(puzzle_input, is_example_input=False):
    max_distance = 32 if is_example_input else 10_000

    coords = [tuple(map(int, line.split(', '))) for line in puzzle_input.split('\n')]
    areas = {(x, y): 0 for x, y in coords}
    proximity_region = []

    x_vals = sorted(x for x, _ in coords)
    y_vals = sorted(y for _, y in coords)
    x_min, x_max = x_vals[0], x_vals[-1]
    y_min, y_max = y_vals[0], y_vals[-1]

    def get_nearest_coord(x, y):
        distances = {(v, w): abs(x-v) + abs(y-w) for v, w in coords}
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        if sum(distances.values()) < max_distance:
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

    return sum(proximity_region)