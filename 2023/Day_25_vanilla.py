# I re-did this one without the help of NetworkX, to see if i could.
# What surprised me is that the vanilla python version turned out to have a lower runtime.
# Apparently NetworkX is adding some unnecessary overhead.

from collections import defaultdict, deque


with open('Advent_of_Code/2023/puzzle_input/25.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    # Construct graph
    graph = defaultdict(list)
    edges = set()
    for line in puzzle_input.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            graph[node1].append(node2)
            graph[node2].append(node1)
            edges.add(tuple(sorted((node1, node2))))

    # Calculate edge betweenness centrality
    edge_betweenness = defaultdict(int)
    for node in graph:
        visited = set([node])
        queue = deque([(node, [])])
        while queue:
            for _ in range(len(queue)):
                curr, path = queue.popleft()
                for edge in path:
                    edge_betweenness[edge] += 1
                for nxt in graph[curr]:
                    if nxt not in visited:
                        visited.add(nxt)
                        edge = tuple(sorted((nxt, curr)))
                        queue.append((nxt, path + [edge]))

    # Remove the three most frequently travelled edges from graph
    most_crucial_edges = sorted(edge_betweenness, key=edge_betweenness.get)[-3:]
    for node1, node2 in most_crucial_edges:
        graph[node1].remove(node2)
        graph[node2].remove(node1)

    # Traverse one of the resulting smaller graphs to find out its size
    visited = set([node])
    queue = [node]
    while queue:
        curr = queue.pop()
        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
        
    # Infer graph sizes and return their product
    size1 = len(visited)
    size2 = len(graph) - size1
    return size1 * size2


print('Part 1:', part1(puzzle_input))