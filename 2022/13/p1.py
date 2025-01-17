from ast import literal_eval

def part1(puzzle_input):

    def compare_item(left, right):
        if type(left) == type(right):

            if type(left) == list: ### both are lists

                for i, l in enumerate(left):

                    if i == len(right): ### right ran out of indices
                        return -1

                    if compare_item(l, right[i]) == 1:
                        return 1

                    elif compare_item(l, right[i]) == -1:
                        return -1

                if len(right) > len(left): ### left ran out of indices
                    return 1
                
            elif left != right: ### both are numbers and not equal
                    return 1 if left < right else -1

        else: ### if one is int the other is list: put the int in a list and compare lists
            return compare_item([left], right) if type(left) == int else compare_item(left, [right])
        
    packets = [[literal_eval(line) for line in s.split('\n')] for s in puzzle_input.split('\n\n')]
    return sum(i for i, (pair) in enumerate(packets, start=1) if compare_item(*pair) == 1)
