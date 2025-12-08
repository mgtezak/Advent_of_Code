from math import dist, prod

def part1(puzzle_input, is_example_input=False):
    limit = 10 if is_example_input else 1000
    junctions = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    n = len(junctions)
    distances = []
    for i in range(n-1):
        for j in range(i+1, n):
            distance = dist(junctions[i], junctions[j])
            distances.append((distance, {i, j}))

    circuits = []
    for _, connection in sorted(distances)[:limit]:
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

    group_sizes = sorted(map(len, circuits))
    return prod(group_sizes[-3:])
