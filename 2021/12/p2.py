from collections import defaultdict
import re

def part2(puzzle_input):
    graph = defaultdict(list)
    for a, b in re.findall(r'(\w+)-(\w+)', puzzle_input):
        graph[a].append(b)
        graph[b].append(a)

    paths = []
    def dfs(node, path, exception_used):
        if node == 'end':
            paths.append(path)
            return
        for adj in graph[node]:
            if adj == 'start':
                continue
            if adj.isupper():
                dfs(adj, path.copy(), exception_used)
            elif adj not in path:
                dfs(adj, path + [adj], exception_used)
            elif not exception_used: 
                dfs(adj, path + [adj], True)

    dfs('start', ['start'], False)
    return len(paths)