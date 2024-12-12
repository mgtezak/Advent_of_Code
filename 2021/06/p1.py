def part1(puzzle_input):
    fish = list(map(int, puzzle_input.split(',')))
    fish_dict = {i: 0 for i in range(9)}
    for f in fish:
        fish_dict[f] += 1

    for _ in range(80):
        new_fish_dict = {i: 0 for i in range(9)}
        for f, count in fish_dict.items():
            if f == 0:
                new_fish_dict[6] += count
                new_fish_dict[8] += count
            else:
                new_fish_dict[f-1] += count
                
        fish_dict = new_fish_dict

    return sum(fish_dict.values())