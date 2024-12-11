def part2(puzzle_input):
    adapters = sorted(map(int, puzzle_input.split('\n')))
    n_paths = {0: 1}  # n_paths[a] = number of distinct paths to reach adapter a
    for a in adapters:
        n_paths[a] = sum(n_paths.get(a-x, 0) for x in range(1, 4))
    return n_paths[max(adapters)]