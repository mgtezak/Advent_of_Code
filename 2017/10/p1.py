def part1(puzzle_input, is_example_input=False):
    n = 5 if is_example_input else 256
    lengths = list(map(int, puzzle_input.split(',')))
    circle = list(range(n))
    pos = 0
    skip_size = 0
    for l in lengths:
        substring = [circle[i % n] for i in range(pos, pos + l)]
        while substring:
            circle[pos] = substring.pop()
            pos = (pos + 1) % n
        pos = (pos + skip_size) % n
        skip_size += 1
        
    return circle[0] * circle[1]