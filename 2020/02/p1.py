def part1(puzzle_input):
    pws = puzzle_input.split('\n')
    count = 0
    for pw in pws:
        count_range, letter, pw = pw.split()
        lower, upper = count_range.split('-')
        count_range = range(int(lower), int(upper)+1)
        letter = letter.strip(':')
        if pw.count(letter) in count_range:
            count += 1
    return count