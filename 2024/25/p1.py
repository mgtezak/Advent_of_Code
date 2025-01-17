def part1(puzzle_input):

    def convert(segment):
        char = segment[0]
        grid = segment.split('\n')
        heights = [0] * 5
        for col in range(5):
            for row in reversed(range(6)):
                if grid[row][col] == char:
                    heights[col] = row
                    break

        return heights
    
    locks, keys = [], []
    for segment in puzzle_input.split('\n\n'):
        if segment.startswith('#'):
            locks.append(convert(segment))
        else:
            keys.append(convert(segment))

    total = 0
    for lock in locks:
        for key in keys:
            for i, j in zip(lock, key):
                if i > j:
                    break
            else:
                total += 1

    return total
