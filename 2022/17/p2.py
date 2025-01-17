from itertools import cycle


def part2(puzzle_input):

    def determine_height(grid):
        for i, line in enumerate(grid):
            if line == list(row):
                return  i - 1
            
    def get_coords(shape, height):
        shape = shape.split()[::-1]
        i, j = 3, height + 4
        return [(x+i, y+j) for y, row in enumerate(shape) for x, char in enumerate(row) if char == '#']

    def move_is_possible(coords, grid):
        return all(grid[y][x] == '.' for x, y in coords)

    def move_sideways(coords, grid):
        jet_idx = next(iter_jet_idx)
        i = 1 if puzzle_input[jet_idx]== '>' else -1
        new_coords = [(x+i, y) for x, y in coords]
        if move_is_possible(new_coords, grid):
            coords = new_coords
        return coords, jet_idx

    def move_down(coords, grid):
        new_coords = [(x, y-1) for x, y in coords]
        if move_is_possible(new_coords, grid):
            return new_coords, False
        return coords, True

    def drop_rock(coords, grid):
        while True:
            coords, jet_idx = move_sideways(coords, grid)
            coords, settled = move_down(coords, grid)
            if settled:
                break
        return coords, jet_idx

    def add_new_rock(grid, shape_index):
        shape = shapes[shape_index]
        height = determine_height(grid)
        coords = get_coords(shape, height)
        coords, jet_idx = drop_rock(coords, grid)
        for x, y in coords:
            grid[y][x] = '#'
        return grid, jet_idx

    iter_jet_idx = cycle(range(len(puzzle_input)))
    shapes = ['####', '.#.\n###\n.#.', '..#\n..#\n###', '#\n#\n#\n#', '##\n##']
    row = '|.......|'
    grid = [['-'] * 9] + [list(row) for _ in range(100_000)] 
    heights = {}
    state_hashes = []
    for rock in range(5000):
        shape_idx = rock % 5
        grid, jet_idx = add_new_rock(grid, shape_idx)
        height = determine_height(grid)
        heights[rock] = height
        hash_value = hash((shape_idx, jet_idx, str(grid[height-1])))
        if hash_value not in state_hashes:
            state_hashes.append(hash_value)
        else:
            cycle_start = state_hashes.index(hash_value)
            cycle_len = len(state_hashes) - cycle_start
            break

    num_cycles = (1_000_000_000_000 - cycle_start) // cycle_len
    remainder = (1_000_000_000_000 - cycle_start) % cycle_len - 1        ### why -1?
    cycle_height = heights[cycle_start + cycle_len] - heights[cycle_start]
    remainder_height = heights[cycle_start + remainder] - heights[cycle_start]
    return heights[cycle_start] + cycle_height * num_cycles + remainder_height
