def part2(puzzle_input):
    expenses = list(map(int, puzzle_input.split('\n')))
    for i, e1 in enumerate(expenses):
        for j, e2 in enumerate(expenses, start=i+1):
            for _, e3 in enumerate(expenses, start=j+1):
                if e1 + e2 + e3 == 2020:
                    return e1 * e2 * e3