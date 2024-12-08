import sympy


def part1(puzzle_input):

    num = int(puzzle_input)
    i = 700000
    while True:
        i += 1
        presents = sum(sympy.divisors(i)) * 10
        if presents >= num:
            break
    
    return i
