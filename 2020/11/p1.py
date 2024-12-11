def part1(puzzle_input):

    puzzle_input = puzzle_input.split()
    width, height = len(puzzle_input[0]), len(puzzle_input)

    def get_adjacent(x, y):
        for i in range(max(0, x-1), min(height, x+2)):
            for j in range(max(0, y-1), min(width, y+2)):
                if (i != x or j != y) and puzzle_input[i][j] == 'L':
                    yield i, j

    graph = {}
    for x in range(height):
        for y in range(width):
            if puzzle_input[x][y] == 'L':
                graph[(x, y)] = set(get_adjacent(x, y))

    occupied = set(graph)
    while True:
        nxt_occupied = set()
        for coords in graph:
            adj_occupied = len(graph[coords] & occupied)
            if (adj_occupied == 0) or (coords in occupied and adj_occupied < 4):
                nxt_occupied.add(coords)

        if occupied == nxt_occupied:
            break

        occupied = nxt_occupied

    return len(occupied)