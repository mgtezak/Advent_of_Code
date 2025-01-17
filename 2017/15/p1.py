import re


def part1(puzzle_input):
    A, B = map(int, re.findall((r'\d+'), puzzle_input))
    mask = (1 << 16) - 1
    mod = (1 << 31) - 1
    matches = 0
    for _ in range(40_000_000):
        A = (A * 16807) % mod
        B = (B * 48271) % mod
        matches += A & mask == B & mask

    return matches
