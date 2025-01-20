def part1(puzzle_input):
    n = 272
    a = puzzle_input
    while len(a) < n:
        b = ''.join('1' if char == '0' else '0' for char in reversed(a))
        a += '0' + b

    checksum = a[:n]
    while len(checksum) % 2 == 0:
        shortened = ''
        for i in range(0, len(checksum), 2):
            shortened += str(len(set(checksum[i:i+2])) % 2)
        checksum = shortened

    return checksum
