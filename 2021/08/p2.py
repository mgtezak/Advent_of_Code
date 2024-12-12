def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    '''
    0:  6  abc efg
    1:  2    c  f   unique
    2:  5  a cde g
    3:  5  a cd fg
    4:  4   bcd f   unique
    5:  5  ab d fg
    6:  6  ab defg
    7:  3  a c  f   unique
    8:  7  abcdefg  unique
    9:  6  abcd fg
    '''

    num_translation = {
        'abcefg': 0, 
        'cf': 1, 
        'acdeg': 2, 
        'acdfg': 3, 
        'bcdf': 4, 
        'abdfg': 5, 
        'abdefg': 6, 
        'acf': 7, 
        'abcdefg': 8, 
        'abcdfg': 9
        }

    output_sum = 0
    for line in lines:
        translation = dict()
        patterns, output = line.split(' | ')
        patterns = sorted(patterns.split(), key=lambda x: len(x))
        
        c_f = set(patterns[0])
        a_c_f = set(patterns[1])
        b_c_d_f = set(patterns[2])
        c_d_e = set(c for i in (6,7,8) for c in 'abcdefg' if c not in patterns[i])
        b_d = b_c_d_f.difference(a_c_f)
        d_e = c_d_e.difference(c_f)

        translation[a_c_f.difference(c_f).pop()] = 'a'
        translation[(b_d.difference(d_e)).pop()] = 'b'
        translation[(c_d_e & c_f).pop()] = 'c'
        translation[(b_d & d_e).pop()] = 'd'
        translation[(d_e.difference(b_d)).pop()] = 'e'
        translation[(c_f.difference(c_d_e)).pop()] = 'f'
        translation[set(patterns[9]).difference(set(translation)).pop()] = 'g'

        output_num = ''
        for n in output.split():
            t = ''
            for c in n:
                t += translation[c]
            t = ''.join(sorted(t))
            output_num += str(num_translation[t])

        output_sum += int(output_num)

    return output_sum