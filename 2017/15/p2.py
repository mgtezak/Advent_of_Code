import re


def part2(puzzle_input):
    A, B = map(int, re.findall((r'\d+'), puzzle_input))
    mask = (1 << 16) - 1
    mod = (1 << 31) - 1
    matches = 0

    def make_generator(val, mul, div):
        while True:
            val = (val * mul) % mod
            if val % div == 0:
                yield val

    A = make_generator(A, 16807, 4)
    B = make_generator(B, 48271, 8)
    for _ in range(5_000_000):
        matches += next(A) & mask == next(B) & mask

    return matches
