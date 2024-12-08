def part2(puzzle_input):
    lines = [list(map(int, line.split())) for line in puzzle_input.split('\n')]

    def validate(triangle):
        half = sum(triangle) / 2
        return True if all(s < half for s in triangle) else False

    return sum(validate((lines[i][j], lines[i+1][j], lines[i+2][j])) for i in range(0, len(lines), 3) for j in range(3))