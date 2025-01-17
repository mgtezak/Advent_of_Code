def part2(puzzle_input):
    sensors = {}
    for line in puzzle_input.split('\n'):
        x1, y1, x2, y2 = map(int, [line.split()[i].strip('xy=,:') for i in (2,3,8,9)])
        sensors[(x1, y1)] = abs(x1 - x2) + abs(y1 - y2)

    def merge_left(ranges):
        if ranges[1][0] <= ranges[0][1] + 1:
            if ranges[1][1] > ranges[0][1]:
                ranges[0][1] = ranges[1][1]
            ranges.pop(1)
            return True
        return False
        
    def get_ranges(row):
        ranges = list()
        for s in sensors:
            x, y = s
            distance_to_row = abs(row - y)
            leftover = max([0, sensors[s] - distance_to_row])
            if leftover:
                low = max(x-leftover, 0) # inclusive boundary
                high = min(x+leftover, 4_000_000) # not inclusive boundary
                ranges.append([low, high])

        ranges.sort()
        while len(ranges) > 1:
            if not merge_left(ranges):
                break

        return ranges

    for y in range(4_000_000):
        r = get_ranges(y)
        if len(r) > 1:
            x = r[0][1] + 1
            break
    
    return x * 4_000_000 + y
