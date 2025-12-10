def part2(puzzle_input):
    corners = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    n = len(corners)

    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((corners[i], corners[i-1])))
        for j in range(i+1, n):
            c1, c2 = sorted((corners[i], corners[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size
