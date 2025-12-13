from functools import cache

def part1(puzzle_input):
    connections = {}
    for line in puzzle_input.splitlines():
        input, outputs = line.split(": ")
        connections[input] = outputs.split()
    
    @cache
    def dfs(device):
        if device == "out":
            return 1
        if (outputs := connections.get(device)) is None:
            return 0
        return sum(dfs(out) for out in outputs)

    return dfs('you')
