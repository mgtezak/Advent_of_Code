def part2(puzzle_input):

    groups = [g.split('\n') for g in puzzle_input.split('\n\n')]
    all_yes_sum = 0

    for g in groups:
        all_yes = set(q for q in g[0] if all(q in g[i] for i, _ in enumerate(g)))
        all_yes_sum += len(all_yes)

    return all_yes_sum