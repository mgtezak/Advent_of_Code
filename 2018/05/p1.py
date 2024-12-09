def part1(puzzle_input):
    remaining = []
    for char in puzzle_input:
        if remaining and abs(ord(char) - ord(remaining[-1])) == 32:
            remaining.pop()
        else :
            remaining.append(char)
    return len(remaining)