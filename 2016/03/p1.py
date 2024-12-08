def part1(puzzle_input):
    lines = [list(map(int, line.split())) for line in puzzle_input.split('\n')]

    def validate(triangle):
        half = sum(triangle) / 2
        return True if all(s < half for s in triangle) else False

    return sum(validate(triangle) for triangle in lines)