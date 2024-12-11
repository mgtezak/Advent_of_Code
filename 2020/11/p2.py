def part2(puzzle_input):

    puzzle_input = puzzle_input.split()
    width, height = len(puzzle_input[0]), len(puzzle_input)

    def get_adjacent(x, y):
        adj = set()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                i, j = x + dx, y + dy
                while i in range(0, height) and j in range(0, width):
                    if puzzle_input[i][j] == 'L':
                        adj.add((i, j))
                        break
                    i, j = i + dx, j + dy
        return adj

    graph = {}
    for x in range(height):
        for y in range(width):
            if puzzle_input[x][y] == '.':
                continue
            graph[(x, y)] = get_adjacent(x, y)

    occupied = set(graph)
    while True:
        nxt_occupied = set()
        for coords in graph:
            adj_occupied = len(graph[coords] & occupied)
            if (adj_occupied == 0) or (coords in occupied and adj_occupied < 5):
                nxt_occupied.add(coords)

        if occupied == nxt_occupied:
            break

        occupied = nxt_occupied

    return len(occupied)