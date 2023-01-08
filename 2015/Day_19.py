with open('Advent_of_Code/2015/puzzle_input/19.txt') as input:
    lines = input.read().split('\n')
    replacements = [line.split(' => ') for line in lines[:-2]]
    formula = lines[-1]

def calc_n_possible_conversions() -> int:
    molecules = set()
    for x, y in replacements:
        for i, _ in enumerate(formula):
            if formula[i:i+len(x)] == x:
                mol = formula[:i] + y + formula[i+len(x):]
                molecules.add(mol)
    return len(molecules)

def calc_fewest_steps() -> int:

    def convert(formula: str) -> str:
        for x, y in replacements:
            for i, _ in enumerate(formula):
                if formula[i:i+len(y)] == y:
                    mol = formula[:i] + x + formula[i+len(y):]
                    yield mol
                    
    def dfs(i: int=0, visited: list=[formula], last: list=[formula], mol: str=formula) -> None:
        if mol == 'e':
            num.append(i)
            return
        else:
            for new_mol in convert(mol):
                if new_mol in visited:
                    continue
                else:
                    visited.append(new_mol)
                    last.append(new_mol)
                    dfs(i + 1, visited, last, new_mol)
                    return
            last.pop()
            dfs(i-1, visited, last, last[-1]) 

    num = []
    dfs()
    return num[0]

print(f'Part 1: {calc_n_possible_conversions()}')
print(f'Part 2: {calc_fewest_steps()}')