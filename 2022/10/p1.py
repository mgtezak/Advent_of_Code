def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    cycle = row = signal_sum = 0
    x = 1
    for line in lines:
        for _ in range(len(line)):
            cycle += 1
            if cycle == 41:
                cycle -= 40
                row += 1
            if cycle == 20:
                signal_sum += x * (cycle + 40 * row)
        
        if line[0] == 'addx':
            x += int(line[1])

    return signal_sum
