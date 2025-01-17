def part1(puzzle_input):
    graph = {}
    for x, line in enumerate(puzzle_input.split()):
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
                visited = set([(x, y)])
                q = set([(x, y)])
            graph[(x, y)] = adjacent

    steps = -1
    while q:
        nxt = set()
        for x1, y1 in q:
            for x2, y2 in graph[(x1, y1)]:
                if (x2, y2) not in visited and (x1, y1) in graph.get((x2, y2), []): 
                    nxt.add((x2, y2))
                    visited.add((x2, y2))
        q = nxt
        steps += 1

    return steps
