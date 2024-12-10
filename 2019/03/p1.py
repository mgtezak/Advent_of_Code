def part1(puzzle_input):
    wires = [wire.split(',') for wire in puzzle_input.split('\n')]

    def get_path(wire):
        x = y = steps = 0
        visited = {}
        directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
        for cmd in wire:
            distance = int(cmd[1:])
            for _ in range(distance):
                x += directions[cmd[0]][0]
                y += directions[cmd[0]][1]      
                steps += 1
                if (x, y) not in visited:
                    visited[(x, y)] = steps
        return visited

    path_1 = get_path(wires[0])
    path_2 = get_path(wires[1])
    isecs = {abs(x) + abs(y): path_1[(x, y)] + path_2[(x, y)] for x, y in path_1 if (x, y) in path_2}
    return min(isecs)