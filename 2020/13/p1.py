import re

def part1(puzzle_input):
    
    earliest, busses = puzzle_input.split()
    earliest = int(earliest)
    wait = float('inf')

    for bus in map(int, re.findall(r'(\d+)', busses)):
        next_departure = bus - earliest % bus
        if next_departure < wait:
            wait = next_departure
            nxt_bus = bus

    return nxt_bus * wait