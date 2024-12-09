path = 'Advent_of_Code/2018/puzzle_input/08.txt'

with open(path) as input:
    nums = list(map(int, input.read().split()))

n = iter(nums)
metadata_sum = 0
root_node_val = 0
parents = []

while not root_node_val:
    children = next(n)                       # processing next node by first checking whether or not it has children
    if parents:
        parents[-1][-1] -= 1                 # one less child needs to be processed

    if children:                             # parse header of parent node
        meta = next(n)
        parents.append([[], meta, children]) # store away parent info for later use

    else:                                    # parse header and evaluate metadata of childless node
        val = sum(next(n) for _ in range(next(n)))
        metadata_sum += val                  # part 1
        parents[-1][0].append(val)           # part 2

        while not parents[-1][-1]:           # evaluate metadata of most recent parent node if no more children to process 
            child_vals, meta, _ = parents.pop()
            m = [next(n) for _ in range(meta)]
            metadata_sum += sum(m)                                                  # part 1
            val = sum(child_vals[i-1] for i in m if i-1 in range(len(child_vals)))  # part 2
            
            if parents:
                parents[-1][0].append(val)
            else:                            # no more parents left to process
                root_node_val = val          # solution to part 2
                break


print(f'Part 1: {metadata_sum}')
print(f'Part 2: {root_node_val}')