def part2(puzzle_input):
    starting_nums = [int(num) for num in puzzle_input.split(',')]
    last_spoken = {int(num): i for i, num in enumerate(starting_nums, start=1)}
    curr = starting_nums[-1]
    for i in range(len(starting_nums), 30_000_000):
        nxt = i - last_spoken.get(curr, i)
        last_spoken[curr] = i
        curr = nxt
    return curr