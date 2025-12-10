def part1(puzzle_input):
    corners = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    n = len(corners)

    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    sizes = []
    for i in range(n-1):
        for j in range(i+1, n):
            sizes.append(get_size(*corners[i], *corners[j]))

    return max(sizes)
