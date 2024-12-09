def part1(puzzle_input):
    box_IDs = [line for line in puzzle_input.split('\n')]
    double = triple = 0
    for b in box_IDs:
        double += 1 if any(b.count(letter) == 2 for letter in b) else 0
        triple += 1 if any(b.count(letter) == 3 for letter in b) else 0
    return double * triple