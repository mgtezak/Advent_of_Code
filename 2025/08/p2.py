from math import dist

def part2(puzzle_input):
    junctions = [list(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    n = len(junctions)
    distances = []
    for i in range(n-1):
        for j in range(i+1, n):
            distance = dist(junctions[i], junctions[j])
            distances.append((distance, {i, j}))

    circuits = []
    for _, connection in sorted(distances):
        overlap = []
        for i, circuit in enumerate(circuits):
            if circuit & connection:
                overlap.append(i)

        if not overlap:
            circuits.append(connection)
        elif len(overlap) == 1:
            circuits[overlap[0]] |= connection
        else:
            circuits[overlap[0]] |= circuits.pop(overlap[1])

        if len(circuits[0]) == n:
            i, j = connection
            return junctions[i][0] * junctions[j][0]
