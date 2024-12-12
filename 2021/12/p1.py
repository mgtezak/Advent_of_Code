from collections import defaultdict
import re

def part1(puzzle_input):
    graph = defaultdict(list)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].append(b)
        graph[b].append(a)

    paths = []
    def dfs(node, path):
        if node == 'end':
            paths.append(path)
            return
        for adj in graph[node]:
            if adj in path:
                continue
            if adj.isupper():
                dfs(adj, path.copy())
            else:
                dfs(adj, path + [adj])

    dfs('start', ['start'])
    return len(paths)