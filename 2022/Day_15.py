path = 'Advent_of_Code/2022/puzzle_input/15.txt'
with open(path) as input:
    coordinates = [[int(s.split()[i].strip('xy=,:')) for i in (2,3,8,9)] for s in input.read().split('\n')]

sensors = {(x1, y1): abs(x1-x2) + abs(y1-y2) for x1, y1, x2, y2 in coordinates}


def get_coverage(row):
    coverage = set()
    for s in sensors:
        x, y = s
        distance_to_row = abs(row - y)
        leftover = sensors[s] - distance_to_row
        for i in range(-leftover, leftover):
            coverage.add(x+i)
    return len(coverage)


def merge_left(ranges):
    if ranges[1][0] <= ranges[0][1] + 1:
        if ranges[1][1] > ranges[0][1]:
            ranges[0][1] = ranges[1][1]
        ranges.pop(1)
        return True


def get_ranges(row):
    ranges = list()
    for s in sensors:
        x, y = s
        distance_to_row = abs(row - y)
        leftover = max([0, sensors[s] - distance_to_row])
        if leftover:
            low = max([x-leftover, 0]) # inclusive boundary
            high = min([x+leftover, 4_000_000]) # not inclusive boundary
            ranges.append([low, high])
    ranges.sort()
    while len(ranges) > 1:
        if not merge_left(ranges):
            break
    return ranges


def find_hole():
    for y in range(4_000_000):
        r = get_ranges(y)
        if len(r) > 1:
            x = r[0][1] + 1
            return x * 4_000_000 + y


print(f'Part 1: {get_coverage(2_000_000)}')
print(f'Part 2: {find_hole()}')