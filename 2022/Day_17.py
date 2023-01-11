from tqdm import tqdm

path = 'Advent_of_Code/2022/puzzle_input/17.txt'
with open(path) as input:
    jet_pattern = input.read()


def get_coords(shape, height):
    shape = shape.split()[::-1]
    i, j = 3, height + 4
    coords = [(x+i, y+j) for y, row in enumerate(shape) for x, char in enumerate(row) if char == '#']
    return coords


def move_is_possible(coords, grid):
    if all(grid[y][x] == '.' for x, y in coords):
        return True


def move_sideways(coords, grid):
    jet_idx = next(iter_jet_idx)
    i = 1 if jet_pattern[jet_idx]== '>' else -1
    new_coords = [(x+i, y) for x, y in coords]
    if move_is_possible(new_coords, grid):
        coords = new_coords
    return coords, jet_idx


def move_down(coords, grid):
    new_coords = [(x, y-1) for x, y in coords]
    if move_is_possible(new_coords, grid):
        coords = new_coords
        settled = False
    else:
        settled = True
    return coords, settled


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


def get_grid(height):
    return [['-'] * 9] + [['|', '.', '.', '.', '.', '.', '.', '.', '|'] for _ in range(height)]


def print_grid(grid, height):
    for i in range(height, -1, -1):
        print(''.join(grid[i]))


def determine_height(grid):
    for i, line in enumerate(grid):
        if line == ['|', '.', '.', '.', '.', '.', '.', '.', '|']:
            return  i - 1
    print('grid is overflowing. increase height')
    return 0


def adjust_height(line):
    if line == ['|', '.', '#', '#', '#', '#', '.', '.', '|'] or line == ['|', '.', '.', '#', '#', '#', '#', '.', '|']:
        return True
 

def idx_cycling_generator(n=5):
    i = 0
    while True:
        yield i%n
        i += 1

def solve():
    grid = get_grid(100000)
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
    def calc_total(target):
        num_cycles = (target - cycle_start) // cycle_len
        remainder = (target - cycle_start) % cycle_len - 1        ### why -1?
        cycle_height = heights[cycle_start + cycle_len] - heights[cycle_start]
        remainder_height = heights[cycle_start + remainder] - heights[cycle_start]
        return heights[cycle_start] + cycle_height * num_cycles + remainder_height

    part1 = calc_total(2022)
    part2 = calc_total(1_000_000_000_000)
    return part1, part2

iter_jet_idx = iter(idx_cycling_generator(len(jet_pattern)))
shapes = ['####', '.#.\n###\n.#.', '..#\n..#\n###', '#\n#\n#\n#', '##\n##']

part1, part2 = solve()
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')