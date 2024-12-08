def part2(puzzle_input):
    nodes = dict()
    for line in puzzle_input.split('\n'):
        line = [s.strip(',()') for s in line.split()]
        node, weight = line[0], int(line[1])
        branches = [] if len(line) == 2 else line[3:]
        nodes[node] = (weight, branches)

    node = (set(nodes) - set(n for k in nodes for n in nodes[k][1])).pop()

    def calc_weight(node): # node's own weight plus weight of branches
        return nodes[node][0] + sum(calc_weight(n) for n in nodes[node][1])

    def is_balanced(node): # True if each branch has the same weight
        return True if len(set(calc_weight(n) for n in nodes[node][1])) == 1 else False

    def calc_avg_weight(node): # average weight of a branch
        return sum(calc_weight(n) for n in nodes[node][1]) / len(nodes[node][1])

    while not is_balanced(node):
        sorted_branches = sorted(nodes[node][1], key=lambda x: -abs(calc_weight(x) - calc_avg_weight(node))) # puts the outlier in front of the list
        outlier = sorted_branches[0]
        node = outlier

    deviation = calc_weight(outlier) - calc_weight(sorted_branches[1])
    return nodes[outlier][0] - deviation
