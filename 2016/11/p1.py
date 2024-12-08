from copy import deepcopy
from itertools import combinations
from collections import deque
import re


def part1(puzzle_input):

    def is_valid(floor):
        microchips = set(i[:2] for i in floor if i[2] == 'M')
        if not microchips or len(microchips) == len(floor):
            return True
        generators = set(i[:2] for i in floor if i[2] == 'G')
        return not (microchips - generators)

    def is_victorious(state):
        return all(state[i] == set() for i in range(3))

    def move(state, obj, floor, nxt_floor):
        new_state = deepcopy(state)

        new_state[floor] -= obj
        if not is_valid(new_state[floor]):
            return False
        
        new_state[nxt_floor] |= obj
        if not is_valid(new_state[nxt_floor]):
            return False
        
        return new_state

    def get_hash(floor, state):
        pair_map = [[None, None] for _ in range(len(pairs))]
        i = 0
        for i, line in enumerate(state):
            for ele in line:
                pair_map[pairs[ele[:2]]][ele[2]=='G'] = str(i)
        return '.'.join(sorted(','.join(pair) for pair in pair_map)) + f'!{floor}'

    def get_valid_moves(state, floor, nxt_floor, n_objs):
        valid_moves = []
        for obj in combinations(state[floor], n_objs):

            nxt_state = move(state, set(obj), floor, nxt_floor)
            if not nxt_state:
                continue

            state_hash = get_hash(nxt_floor, nxt_state)
            if state_hash in hashmap:
                continue

            hashmap.add(state_hash)
            valid_moves.append((nxt_floor, nxt_state))

        return valid_moves

    state = []
    for line in puzzle_input.split('\n'):
        line = re.sub(r'-compatible|enerator|icrochip', '', line)
        state.append(set(name.upper() + type.upper() for name, type in re.findall(r'(\w{2})\w+ (g|m)', line)))
    
    pairs = {x: i for i, x in enumerate(re.findall(r'(\w\w)G', ' '.join(' '.join(row) for row in state)))}

    hashmap = set()
    queue = deque([(0, state)])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            floor, state = queue.popleft()

            if is_victorious(state):
                return steps
            
            if floor < 3:   # if you can move 2 objs up, don't bother moving only 1 up
                if move_2_up := get_valid_moves(state, floor, floor+1, 2):  
                    queue.extend(move_2_up)
                else:
                    queue.extend(get_valid_moves(state, floor, floor+1, 1))

            if floor > 0:   # never move more than 1 obj down
                queue.extend(get_valid_moves(state, floor, floor-1, 1))

        steps += 1