from collections import deque
from hashlib import md5


def part1(puzzle_input):
    move = [
        (-1, 0, 'U'), 
        (1, 0, 'D'), 
        (0, -1, 'L'), 
        (0, 1, 'R')
    ]
    queue = deque([(0, 0, puzzle_input)])
    while queue:
        x, y, key = queue.popleft()
        if x not in range(4) or y not in range(4):
            continue

        if x == y == 3:
            return key[len(puzzle_input):]

        doors = md5(key.encode()).hexdigest()[:4]
        for i, door in enumerate(doors):
            if door in 'bcdef':
                r, c, d = move[i]
                queue.append((x+r, y+c, key+d))
