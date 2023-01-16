path = 'Advent_of_Code/2019/puzzle_input/01.txt'
from math import floor

with open(path) as input:
    data = input.read().split('\n')

def calculate_fuel(x, part2=False):
    fuel = floor(x / 3) - 2
    if fuel < 0:
        fuel = 0
    if fuel >= 9 and part2:
        fuel += calculate_fuel(fuel, part2=True)
    return fuel

part1 = sum([calculate_fuel(int(x)) for x in data])
part2 = sum([calculate_fuel(int(x), part2=True) for x in data])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')