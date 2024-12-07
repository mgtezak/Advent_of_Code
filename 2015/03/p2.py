def part2(puzzle_input):

    def get_coords(moves, x=0, y=0):
        directions = {'v': (0, -1), '^': (0, 1), '<': (-1, 0), '>': (1, 0)}
        visited = {(x, y)}
        for move in moves:
            x += directions[move][0]
            y += directions[move][1]
            visited.add((x, y))
        return visited

    santa_moves, robo_moves = puzzle_input[0::2], puzzle_input[1::2]
    santa_coords, robo_coords = get_coords(santa_moves), get_coords(robo_moves)
    return len(santa_coords | robo_coords)
