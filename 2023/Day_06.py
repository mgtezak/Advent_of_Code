import re
import math

with open('Advent_of_Code/2023/puzzle_input/06.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    times, distances = puzzle_input.split('\n')
    times = map(int, re.findall('\d+', times))
    distances = map(int, re.findall('\d+', distances))
    total = 1
    for t, d in zip(times, distances):
        wins = 0
        for speed in range(1, t):
            travelled = (t-speed) * speed
            if travelled > d:
                wins += 1
            elif wins:
                break

        total *= wins
    
    return total
        
 
def part2(puzzle_input):
    time, distance = puzzle_input.split('\n')
    time = int(''.join(re.findall('\d+', time)))
    distance = int(''.join(re.findall('\d+', distance)))
    exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
    min_acceleration = int(exact_acceleration + 1)
    return time - 2*min_acceleration + 1


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))