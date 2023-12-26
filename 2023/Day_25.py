import networkx as nx

with open('Advent_of_Code/2023/puzzle_input/25.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    edges = []
    for line in puzzle_input.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            edges.append((node1, node2))

    graph = nx.from_edgelist(edges)
    min_edge_cut = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(min_edge_cut)
    size1, size2 = [len(c) for c in nx.connected_components(graph)]
    return size1 * size2


print('Part 1:', part1(puzzle_input))