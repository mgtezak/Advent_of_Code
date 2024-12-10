def part2(puzzle_input):
    data = puzzle_input.split('\n')

    def calculate_fuel(x):
        fuel = x // 3 - 2
        fuel = max(0, fuel)
        if fuel >= 9:
            fuel += calculate_fuel(fuel)
        return fuel

    return sum(calculate_fuel(int(x)) for x in data)