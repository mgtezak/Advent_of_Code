def part2(puzzle_input):

    def convert(formula: str) -> str:
        for x, y in replacements:
            for i in range(len(formula)):
                if formula[i:i+len(y)] == y:
                    mol = formula[:i] + x + formula[i+len(y):]
                    yield mol
                    
    def dfs(i: int, visited: list, last: list, mol: str) -> None:
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

    lines = puzzle_input.split('\n')
    replacements = [line.split(' => ') for line in lines[:-2]]
    formula = lines[-1]
    num = []
    dfs(0, [formula], [formula], formula)
    return num[0]