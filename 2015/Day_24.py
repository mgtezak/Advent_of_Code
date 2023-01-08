import itertools
import numpy as np

with open('Advent_of_Code/2015/puzzle_input/24.txt') as input:
    data = list(map(int, input.read().split()))

def find_quantum_entanglement(part2: bool=False) -> int:
    '''Increments the number of elements until combination with least amount of elements is found 
    which reaches the target. Returns the lowest "quantum entanglement" (product of elements).'''
    target = sum(data)/3 if not part2 else sum(data)/4
    i = 0
    combinations = []
    while not combinations: 
        i += 1
        combinations = [c for c in itertools.combinations(data, i) if sum(c) == target]  
    quantum_entanglement = [np.prod(c) for c in combinations]
    return min(quantum_entanglement)
    
print(f'Part 1: {find_quantum_entanglement()}')
print(f'Part 2: {find_quantum_entanglement(part2=True)}')