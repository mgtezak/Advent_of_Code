import re
from collections import defaultdict


def part2(puzzle_input):
    graph = defaultdict(set)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].add(b)
        graph[b].add(a)

    def bron_kerbosch(selected, candidates, excluded):
        if not candidates and not excluded:
            return selected
        
        max_clique = set()
        for v in candidates.copy():
            clique = bron_kerbosch(
                selected.union({v}), 
                candidates.intersection(graph[v]), 
                excluded.intersection(graph[v])
            )
            max_clique = max(max_clique, clique, key=len)
            candidates.remove(v)
            excluded.add(v)

        return max_clique

    max_clique = bron_kerbosch(set(), set(graph), set())
    return ','.join(sorted(max_clique))
