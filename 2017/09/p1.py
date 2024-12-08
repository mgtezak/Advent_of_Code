def part1(puzzle_input):
    score = 0
    level = 0
    garbage = False
    ignore_next = False
    for c in puzzle_input:
        if garbage:
            if ignore_next:
                ignore_next = False
            elif c == '!':
                ignore_next = True
            elif c == '>':
                garbage = False
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
        elif c == '<':
            garbage = True
    return score
