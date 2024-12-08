def part1(puzzle_input):
    graph = {}
    for line in puzzle_input.split('\n'):
        node, paths = line.split(' <-> ')
        graph[int(node)] = [int(p) for p in paths.split(', ')]

    count = 0
    queue = set([0])
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        queue |= set(n for n in graph[node]) - queue - visited
        count += 1

    return count
