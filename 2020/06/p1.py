def part1(puzzle_input):

    groups = [g.split('\n') for g in puzzle_input.split('\n\n')]
    any_yes_sum = 0 # part 1

    for g in groups:
        any_yes = set(q for p in g for q in p)
        any_yes_sum += len(any_yes)

    return any_yes_sum