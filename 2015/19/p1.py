def part1(puzzle_input):

    lines = puzzle_input.split('\n')
    replacements = [line.split(' => ') for line in lines[:-2]]
    formula = lines[-1]

    molecules = set()
    for x, y in replacements:
        for i in range(len(formula)):
            if formula[i:i+len(x)] == x:
                mol = formula[:i] + y + formula[i+len(x):]
                molecules.add(mol)

    return len(molecules)