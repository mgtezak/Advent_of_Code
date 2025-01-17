def part2(puzzle_input):
    dec_key = 811589153
    indexed_nums = [(i, n * dec_key) for i, n in enumerate(map(int, puzzle_input.split('\n')))]
    mixed = indexed_nums.copy()
    l = len(mixed) - 1

    for _ in range(10):
        for i, n in indexed_nums:
            idx = mixed.index((i, n))
            new_idx = (idx + n) % l
            mixed.remove((i, n))
            mixed.insert(new_idx, (i, n))

    zero_idx = [i for i, tup in enumerate(mixed) if not tup[1]].pop()
    return sum(mixed[(zero_idx + i) % (l+1)][1] for i in (1000, 2000, 3000))
