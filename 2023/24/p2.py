import sympy as sp


def part2(puzzle_input):
    first_three_hailstones = []
    for line in puzzle_input.split('\n')[:3]:
        nums = line.replace('@', ',').split(',')
        first_three_hailstones.append(tuple(map(int, nums)))

    x, y, z, dx, dy, dz, *time = sp.symbols('x, y, z, dx, dy, dz, t1, t2, t3')

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, first_three_hailstones):
        equations.append(sp.Eq(x + t*dx, h[0] + t*h[3]))
        equations.append(sp.Eq(y + t*dy, h[1] + t*h[4]))
        equations.append(sp.Eq(z + t*dz, h[2] + t*h[5]))

    solution = sp.solve(equations, (x, y, z, dx, dy, dz, *time)).pop()
    return int(sum(solution[:3]))
