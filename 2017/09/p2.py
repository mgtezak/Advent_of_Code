def part2(puzzle_input):
    score = 0
    level = 0
    garbage = False
    ignore_next = False
    garbage_chars = 0   # part 2
    for c in puzzle_input:
        if garbage:
            if ignore_next:
                ignore_next = False
            elif c == '!':
                ignore_next = True
            elif c == '>':
                garbage = False
            else:
                garbage_chars += 1   # part 2
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
        elif c == '<':
            garbage = True
    return garbage_chars
