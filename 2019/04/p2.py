def part2(puzzle_input):

    def passes(n):   
        s = str(n)
        if any(int(s[i]) > int(s[i+1]) for i in range(5)):
            return False
        groups = [s.count(digit) for digit in set(s)]
        return 2 in groups

    start, end = [int(n) for n in puzzle_input.split('-')]
    return len([n for n in range(start, end) if passes(n)])
