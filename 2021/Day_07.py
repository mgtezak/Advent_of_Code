path = 'Advent_of_Code/2021/puzzle_input/07.txt'

with open(path) as input:
    crabs = list(map(int, input.read().split(',')))


def calc_fuel(pos, part2=False):
    fuel = 0
    for c in crabs:
        dist = abs(pos - c)
        if not part2:
            fuel += dist
        else:
            fuel += dist * (dist+1) / 2
            
    return fuel


def find_optimal_alignment(part2=False):
    i = 0
    results = []
    while True:
        fuel = calc_fuel(i, part2)

        if results and fuel > results[-1]:
            break

        results.append(fuel)
        i += 1

    return int(results.pop())


print(f'Part 1: {find_optimal_alignment()}')
print(f'Part 2: {find_optimal_alignment(True)}')