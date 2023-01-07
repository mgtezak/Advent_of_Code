with open('Advent_of_Code/2015/puzzle_input/17.txt') as input:
    containers = list(map(int, input.read().split('\n')))

def get_combinations(containers: list, target: int) -> list:
    '''finds all combinations of available container sizes that add up to the target value'''

    def dfs(i: int=0, current: list=[], total: int=0) -> None:
        '''recursive depth-first-search algorhythm that keeps adding containers until target is either reached or surpassed'''

        if total == target:
            combinations.append(current.copy())
            return

        elif i >= len(containers) or total > target:
            return

        current.append(containers[i])
        dfs(i + 1, current, total + containers[i])
        current.pop()
        dfs(i + 1, current, total)
    
    combinations = []
    dfs()

    return combinations

combinations = get_combinations(containers, 150)
n_combinations = len(combinations)

comb_lengths = sorted([len(c) for c in combinations])
min_length = [l for l in comb_lengths if l == comb_lengths[0]]
n_min_length = len(min_length)

print(f'Part 1: {n_combinations}')
print(f'Part 2: {n_min_length}')