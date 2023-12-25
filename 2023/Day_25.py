import networkx as nx
import math

with open('Advent_of_Code/2023/puzzle_input/25.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    edges = []
    for line in puzzle_input.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            edges.append((node1, node2))

    graph = nx.from_edgelist(edges)
    edge_betweenness = nx.edge_betweenness_centrality(graph)
    most_crucial_edges = sorted(edge_betweenness, key=edge_betweenness.get)[-3:]
    graph.remove_edges_from(most_crucial_edges)
    group_sizes = [len(c) for c in nx.connected_components(graph)]
    return math.prod(group_sizes)


print('Part 1:', part1(puzzle_input))