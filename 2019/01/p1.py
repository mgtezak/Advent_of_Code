def part1(puzzle_input):
    data = puzzle_input.split('\n')

    def calculate_fuel(x):
        fuel = x // 3 - 2
        return max(0, fuel)

    return sum(calculate_fuel(int(x)) for x in data)