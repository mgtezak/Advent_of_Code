'''Technically i would need to be set to 0. But after a lot of trial 
and error I figured out that the solution was above 700 thousand. 
My first solution ran for more than 45 min. 
Using sympy sped things up considerably'''

import sympy

# my puzzle input:
num = 33100000

# part 1:
i = 700000
part1 = None
while not part1:
    i += 1
    presents = sum(sympy.divisors(i)) * 10
    if presents >= num:
        part1 = i

# part 2:
i = 700000
part2 = None
while not part2:
    i += 1
    presents = sum([div for div in sympy.divisors(i) if div > i / 50]) * 11
    if presents >= num:
        part2 = i

print(f'Part 1: {part1}')
print(f'Part 2: {part2}') 