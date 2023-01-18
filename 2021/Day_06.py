path = 'Advent_of_Code/2021/puzzle_input/06.txt'

with open(path) as input:
    fish = list(map(int, input.read().split(',')))


def get_fishcount_n_days(n):
    fish_dict = {i: 0 for i in range(9)}
    for f in fish:
        fish_dict[f] += 1

    for _ in range(n):
        new_fish_dict = {i: 0 for i in range(9)}
        for f, count in fish_dict.items():
            if f == 0:
                new_fish_dict[6] += count
                new_fish_dict[8] += count
            else:
                new_fish_dict[f-1] += count
        fish_dict = new_fish_dict

    return sum(fish_dict.values())

print(f'Part 1: {get_fishcount_n_days(80)}')
print(f'Part 2: {get_fishcount_n_days(256)}')