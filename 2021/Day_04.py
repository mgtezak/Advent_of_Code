path = 'Advent_of_Code/2021/puzzle_input/04.txt'

with open(path) as input:
    input = input.read().split('\n\n')

nums = [int(n) for n in input[0].split(',')]
boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in input[1:]]

marked_rows = {b: {r: 0 for r in range(5)} for b in range(len(boards))}
marked_cols = {b: {c: 0 for c in range(5)} for b in range(len(boards))}
marked_cords = {b: set() for b in range(len(boards))}

def get_score(i, num):
    score = 0
    for r, row in enumerate(boards[i]):
        for c, n in enumerate(row):
            if (r, c) not in marked_cords[i]:
                score += n
    return score * num

unfinished = [b for b in range(len(boards))]
while unfinished:
    num = nums.pop(0)
    for i, board in enumerate(boards):
        if i in unfinished:
            for r, row in enumerate(boards[i]):
                for c, n in enumerate(row):
                    if n == num:
                        marked_rows[i][r] += 1
                        marked_cols[i][c] += 1
                        marked_cords[i].add((r, c))
                        if marked_rows[i][r] == 5 or marked_cols[i][c] == 5:
                            unfinished.remove(i)
                            if len(unfinished) == len(boards) - 1:
                                winner = get_score(i, num)
                            elif not unfinished:
                                loser = get_score(i, num)

print(f'Part 1: {winner}')
print(f'Part 2: {loser}')