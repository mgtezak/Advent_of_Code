with open('Advent_of_Code/2015/puzzle_input/03.txt') as input:
    moves = input.read()

def get_visited_coords(moves: str=moves, x: int=0, y: int=0):
    directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
    visited = {(x, y)}
    for move in moves:
        x += directions[move][0]
        y += directions[move][1]
        visited.add((x, y))
    return visited

part1 = len(get_visited_coords())
santa, robo = moves[0::2], moves[1::2]
part2 = len(get_visited_coords(santa).union(get_visited_coords(robo)))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')