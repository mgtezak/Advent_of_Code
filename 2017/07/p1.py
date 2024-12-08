def part1(puzzle_input):
    nodes = dict()
    for line in puzzle_input.split('\n'):
        line = [s.strip(',()') for s in line.split()]
        node, weight = line[0], int(line[1])
        branches = [] if len(line) == 2 else line[3:]
        nodes[node] = (weight, branches)

    return (set(nodes) - set(n for k in nodes for n in nodes[k][1])).pop()
