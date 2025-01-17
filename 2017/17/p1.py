def part1(puzzle_input):
    steps = int(puzzle_input) + 1
    pos = 0
    spinlock = [0]
    for i in range(1, 2018):
        pos = (pos + steps) % i
        spinlock.insert(pos, i)

    idx = (spinlock.index(2017) + 1) % 2018
    return spinlock[idx]
