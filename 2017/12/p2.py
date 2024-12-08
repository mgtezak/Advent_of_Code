def part2(puzzle_input):
    graph = {}
    for line in puzzle_input.split('\n'):
        node, paths = line.split(' <-> ')
        graph[int(node)] = [int(p) for p in paths.split(', ')]

    count = 0
    visited = set()
    for node, paths in graph.items():
        if node in visited:
            continue
        count += 1
        queue = set([node])
        while queue:
            node = queue.pop()
            visited.add(node)
            queue |= set(n for n in graph[node]) - queue - visited
    return count
