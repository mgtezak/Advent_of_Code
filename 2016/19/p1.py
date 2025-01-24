def part1(puzzle_input):
    circle = list(range(1, int(puzzle_input) + 1))
    offset = 0
    while len(circle) > 1:
        odd_length = len(circle) % 2
        circle = [circle[i] for i in range(offset, len(circle), 2)]
        offset ^= odd_length

    return circle[0]
