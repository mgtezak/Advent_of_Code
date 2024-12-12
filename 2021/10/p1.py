def part1(puzzle_input):
    lines = puzzle_input.split('\n')

    # Part 1:
    syntax_err_score = 0
    syntax_err = dict(zip(')]}>', [3, 57, 1197, 25137]))


    # Part 2:
    autocomp_scores = []
    autocomp = dict(zip('([{<', [1, 2, 3, 4]))

    brackets = dict(zip(')]}>', '([{<'))
    for line in lines:
        open_brackets = []
        for b in line:
            if b in '([{<':
                open_brackets.append(b)
            else:
                if open_brackets.pop() == brackets[b]:
                    continue
                else:   # line must be corrupted (part 1)
                    syntax_err_score += syntax_err[b]
                    break

        else:   # line must be uncorrupted but incomplete (part 2)
            score = 0
            while open_brackets:
                score = 5 * score + autocomp[open_brackets.pop()]
            autocomp_scores.append(score)

    middle_autocomp_score = sorted(autocomp_scores)[len(autocomp_scores)//2]

    return syntax_err_score