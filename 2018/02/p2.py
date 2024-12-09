def part2(puzzle_input):
    box_IDs = [line for line in puzzle_input.split('\n')]
    differ_by_1 = None
    for i, b in enumerate(box_IDs):        
        if not differ_by_1:
            for other_b in box_IDs[i+1:]:
                differ = sum(1 if b[i] != other_b[i] else 0 for i in range(len(b)))
                if differ == 1:
                    differ_by_1 = {b, other_b}

    a, b = differ_by_1
    return ''.join(letter for i, letter in enumerate(a) if letter == b[i])