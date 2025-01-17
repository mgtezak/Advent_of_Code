def part1(puzzle_input):
    indexed_nums = [(i, n) for i, n in enumerate(map(int, puzzle_input.split('\n')))]
    mixed = indexed_nums.copy()
    l = len(mixed) - 1

    for i, n in indexed_nums:
        idx = mixed.index((i, n))
        new_idx = (idx + n) % l
        mixed.remove((i, n))
        mixed.insert(new_idx, (i, n))

    zero_idx = [i for i, tup in enumerate(mixed) if not tup[1]].pop()
    return sum(mixed[(zero_idx + i) % (l+1)][1] for i in (1000, 2000, 3000))
