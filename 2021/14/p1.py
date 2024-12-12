from collections import Counter
import re

def part1(puzzle_input):

    # Parse input
    molecule, reactions = puzzle_input.split('\n\n')

    # Create replacement dictionary
    replace = {}
    for x, y, z in re.findall(r'(\w)(\w) -> (\w)', reactions):
        replace[x + y] = z + y

    # Execute 10 transitions steps
    for _ in range(10):
        new_molecule = molecule[0]
        for i in range(len(molecule)-1):
            new_molecule += replace[molecule[i:i+2]]
        molecule = new_molecule

    # Return difference between most and least frequent letter
    letter_counts = sorted(Counter(molecule).values())
    return letter_counts[-1] - letter_counts[0]