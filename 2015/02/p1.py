def part1(puzzle_input):
    total_paper = 0
    for line in puzzle_input.split('\n'):
        a, b, c = map(int, line.split('x'))
        sides = [a*b, b*c, a*c]
        total_paper += sum(sides) * 2 + min(sides)
    return total_paper
