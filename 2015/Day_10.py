# solution using itertools
import itertools

with open('Advent_of_Code/2015/puzzle_input/10.txt') as input:
    input_num = input.read()

def look_and_say(num, iterations):
    for i in range(iterations):
        num = ''.join(str(len(list(g))) + str(n) for n, g in itertools.groupby(num))
    return num

first_num = look_and_say(input_num, 40)
second_num = look_and_say(first_num, 10)


# alternative solution using regex
import re

def replace(match_obj):
    group = match_obj.group(1)
    return str(len(group)) + group[0]

def solve_using_re(number, iterations):
    for _ in range(iterations):
        number = pattern.sub(replace, number)
    return number

pattern = re.compile(r'((\d)\2*)')
first_num = solve_using_re(input_num, 40)
second_num = solve_using_re(first_num, 10)

print(f'Part 1: {len(first_num)}')
print(f'Part 2: {len(second_num)}')