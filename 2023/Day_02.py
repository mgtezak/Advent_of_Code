with open('Advent_of_Code/2023/puzzle_input/02.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    possible = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        game = game.split(': ')[1]
        for hand in game.split('; '):
            is_impossible = False
            for subset in hand.split(', '):
                n, color = subset.split()
                if int(n) > possible[color]:
                    is_impossible = True
                    break
            if is_impossible:
                break
        else:
            possible_games += id

    return possible_games


def part2(puzzle_input):
    power = 0
    for game in puzzle_input.split('\n'):
        game = game.split(': ')[1]
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for hand in game.split('; '):
            for subset in hand.split(', '):
                n, color = subset.split()
                max_number[color] = max(int(n), max_number[color])

        power += max_number['red'] * max_number['green'] * max_number['blue']

    return power


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))