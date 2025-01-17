def part2(puzzle_input):
    grid = puzzle_input.split()
    graph = {}
    for x, line in enumerate(grid):
        for y, tile in enumerate(line):
            adjacent = []
            if tile in '-J7S':
                adjacent.append((x, y-1))
            if tile in '-FLS':
                adjacent.append((x, y+1))
            if tile in '|F7S':
                adjacent.append((x+1, y))      
            if tile in '|LJS':
                adjacent.append((x-1, y))
            if tile == 'S':
                tile_q = set([(x, y)])
            graph[(x, y)] = adjacent

    pipes = set()
    while tile_q:
        nxt = set()
        for x1, y1 in tile_q:
            for x2, y2 in graph[(x1, y1)]:
                if (x1, y1) not in graph.get((x2, y2), []):
                    continue
                pipe = (*sorted((x1, x2)), *sorted((y1, y2)))
                if pipe not in pipes:
                    pipes.add(pipe)
                    nxt.add((x2, y2))
        tile_q = nxt

    m, n = len(grid), len(grid[0])
    visited = set()
    corner_q = [(0, 0)]

    while corner_q:
        x, y = corner_q.pop()
        requirements = (x > 0, y < n, x < m, y > 0)
        adjacent = ((x-1, y), (x, y+1), (x+1, y), (x, y-1))
        tile_pairs = ((x-1, x-1, y-1, y),   # up
                      (x-1, x, y, y),       # right
                      (x, x, y-1, y),       # down
                      (x-1, x, y-1, y-1))   # left
        for req, corner, tile_pair in zip(requirements, adjacent, tile_pairs):
            if req and corner not in visited and tile_pair not in pipes:
                visited.add(corner)
                corner_q.append(corner)

    total = m * n - len(pipes)
    for i in range(m):
        for j in range(n):
            corners = ((i, j), (i+1, j), (i, j+1), (i+1, j+1))
            if all(c in visited for c in corners):
                total -= 1

    return total
