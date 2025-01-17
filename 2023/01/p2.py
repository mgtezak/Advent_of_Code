import re


def part2(puzzle_input):

    def get_digit(x):
        return x if x.isnumeric() else str(letter_digits.index(x))
    
    letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'  
    total = 0

    for line in puzzle_input.split('\n'):
        digits = re.findall(regex, line)
        total += int(get_digit(digits[0]) + get_digit(digits[-1]))

    return total
