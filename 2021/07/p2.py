def part2(puzzle_input):

    def calc_fuel(pos):
        fuel = 0
        for c in crabs:
            dist = abs(pos - c)
            fuel += dist * (dist+1) / 2 
        return fuel
    
    crabs = list(map(int, puzzle_input.split(',')))
    i = 0
    results = []
    while True:
        fuel = calc_fuel(i)
        if results and fuel > results[-1]:
            break
        results.append(fuel)
        i += 1
    return int(results.pop())
