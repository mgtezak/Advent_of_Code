from collections import Counter
from datetime import datetime

def part1(puzzle_input):
    data = [line.split() for line in puzzle_input.split('\n')]
    timeline = []
    for line in data:
        date_str = ''.join(line[0] + line[1]).strip('[]') 
        date = datetime.strptime(date_str, '%Y-%m-%d%H:%M')
        timeline.append((date, line[2:]))
    timeline.sort()    
    sleep_record = {}
    guard = None
    asleep = False
    for i, event in enumerate(timeline):
        if event[1][0] == 'Guard':
            guard = int(event[1][1].strip('#'))
            if guard not in sleep_record:
                sleep_record[guard] = []
        elif event[1][0] == 'wakes':
            mins = [m for m in range(asleep, event[0].minute)]
            sleep_record[guard] += mins
            asleep = False
        else:
            asleep = event[0].minute
        
    elf_1 = max(sleep_record, key=lambda x: len(sleep_record.get(x)))
    min_counter = Counter(sleep_record[elf_1])
    minute_1 = max(min_counter, key=min_counter.get)
    return elf_1 * minute_1