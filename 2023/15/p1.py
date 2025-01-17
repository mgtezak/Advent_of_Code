def part1(puzzle_input):
    total = 0
    for step in puzzle_input.split(','):
        current_val = 0
        for char in step:
            current_val += ord(char)
            current_val *= 17
            current_val %= 256
            
        total += current_val

    return total
