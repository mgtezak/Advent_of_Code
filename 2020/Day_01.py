path = 'Advent_of_Code/2020/puzzle_input/01.txt'

with open(path) as input:
    expenses = list(map(int, input.read().split('\n')))

def find_entries_1():
    for i, e1 in enumerate(expenses):
        for _, e2 in enumerate(expenses, start=i+1):
            if e1 + e2 == 2020:
                return e1 * e2

def find_entries_2():
    for i, e1 in enumerate(expenses):
        for j, e2 in enumerate(expenses, start=i+1):
            for _, e3 in enumerate(expenses, start=j+1):
                if e1 + e2 + e3 == 2020:
                    return e1 * e2 * e3

print(f'Part 1: {find_entries_1()}')
print(f'Part 2: {find_entries_2()}')

