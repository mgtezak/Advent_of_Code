def part1(puzzle_input, is_example_input=False):
    target = 25 if is_example_input else 150

    def dfs(i: int, current: list, total: int) -> None:    
        '''recursive depth-first-search algorithm that keeps adding containers until target is either reached or surpassed'''

        if total == target:
            combinations.append(current.copy())
            return

        elif i >= len(containers) or total > 150:
            return

        current.append(containers[i])
        dfs(i + 1, current, total + containers[i])
        current.pop()
        dfs(i + 1, current, total)

    containers = list(map(int, puzzle_input.split('\n')))
    combinations = []
    dfs(0, [], 0)
    return len(combinations)
