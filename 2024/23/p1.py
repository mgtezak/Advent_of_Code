import re
from collections import defaultdict


def part1(puzzle_input):
    graph = defaultdict(set)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].add(b)
        graph[b].add(a)

    candidates = [c for c in graph if c.startswith('t')]
    t_triples = set()
    for t in candidates:
        for a in graph[t]:
            for b in graph[a]:
                if b in graph[t]:
                    t_triples.add(tuple(sorted([t, a, b])))

    return len(t_triples)
