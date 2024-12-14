import re


def part1(puzzle_input):
    total = 0
    tolerance = 0.0001
    for machine in puzzle_input.split('\n\n'):
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        A = (bx*y - by*x) / (bx*ay - by*ax)
        B = (x-ax*A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B

    return int(total)
