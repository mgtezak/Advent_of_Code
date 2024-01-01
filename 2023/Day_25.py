import networkx as nx
from itertools import combinations


with open('Advent_of_Code/2023/puzzle_input/25.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    graph = nx.Graph()
    for line in puzzle_input.split('\n'):
        node1, connected = line.split(': ')
        for node2 in connected.split():
            graph.add_edge(node1, node2, capacity=1)

    for node1, node2 in combinations(graph.nodes, 2):
        cuts, partitions = nx.minimum_cut(graph, node1, node2)
        if cuts == 3:
            break

    return  len(partitions[0]) * len(partitions[1])


print('Part 1:', part1(puzzle_input))