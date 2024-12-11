def part2(puzzle_input):
    pws = puzzle_input.split('\n')
    count = 0
    for pw in pws:
        indices, letter, pw = pw.split()
        i, j = map(lambda x: int(x)-1, indices.split('-'))
        letter = letter.strip(':')
        if (pw[i] == letter and not pw[j] == letter) or (not pw[i] == letter and pw[j] == letter):
            count += 1
    return count