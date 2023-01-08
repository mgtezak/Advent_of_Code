with open('Advent_of_Code/2015/puzzle_input/25.txt') as input:
    instruction = input.read().split()
    row, col = [int(instruction[i].strip(',.')) for i in (-1, -3)]

def get_n_iter(x: int, y: int) -> int:
    col = row = i = 1
    while (col, row) != (x, y):
        if col > 1:
            row += 1
            col -= 1
        else:
            col = row + 1
            row = 1
        i += 1
    return i

def get_code(n_iter: int) -> int:
    code = 20151125
    for _ in range(n_iter-1):
        code = code * 252533 % 33554393
    return code

print(f'Solution: {get_code(get_n_iter(col, row))}')