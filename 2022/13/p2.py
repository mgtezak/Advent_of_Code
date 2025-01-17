from ast import literal_eval
from functools import cmp_to_key


def part2(puzzle_input):

    def compare_item(left, right):
        if type(left) == type(right):

            if isinstance(left, list): ### both are lists

                for i, _ in enumerate(left):

                    if i == len(right): ### right ran out of indices
                        return -1

                    if compare_item(left[i], right[i]) == 1:
                        return 1

                    elif compare_item(left[i], right[i]) == -1:
                        return -1

                if len(right) > len(left): ### left ran out of indices
                    return 1
                
            elif left != right: ### both are numbers and not equal
                    return 1 if left < right else -1

        else: ### if one is int the other is list: put the int in a list and compare lists
            return compare_item([left], right) if type(left) == int else compare_item(left, [right])
        
    packets = [[literal_eval(line) for line in s.split('\n')] for s in puzzle_input.split('\n\n')]
    all_packets = [l for packet in packets for l in packet] + [[[2]], [[6]]]
    sorted_packets = ['index 0'] + sorted(all_packets, key=cmp_to_key(compare_item), reverse=True)
    return sorted_packets.index([[2]]) * sorted_packets.index([[6]])
