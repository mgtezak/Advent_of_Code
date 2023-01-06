with open('Advent_of_Code/2015/puzzle_input/03.txt') as input:
    moves = input.read()

def one(moves=moves, x=0, y=0):
    directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
    visited = {(x, y)}
    for move in moves:
        x += directions[move][0]
        y += directions[move][1]
        visited.add((x, y))
    return visited

def two():
    santa, robo = moves[0::2], moves[1::2]
    return one(santa).union(one(robo))

print(f'Part 1: {len(one())}')
print(f'Part 2: {len(two())}')