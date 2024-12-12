def part1(puzzle_input):
    lines = puzzle_input.split('\n')
    unique_nums = 0
    for line in lines:
        _, output = line.split(' | ')
        for v in output.split():
            if len(v) in (2, 3, 4, 7):
                unique_nums += 1
    return unique_nums
