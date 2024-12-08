import sympy


def part2(puzzle_input):
    
    num = int(puzzle_input)
    i = 700000
    while True:
        i += 1
        presents = sum(div for div in sympy.divisors(i) if div > i / 50) * 11
        if presents >= num:
            break
    
    return i
