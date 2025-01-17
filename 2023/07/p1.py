from collections import Counter
from functools import cmp_to_key
import re


def part1(puzzle_input):

    def get_type(hand):
        counts = sorted(Counter(hand).values(), reverse=True)
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0  
      
    def compare(a, b):
        type_a = get_type(a[0])
        type_b = get_type(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    cards = '23456789TJQKA'
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, puzzle_input)
    hands.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)

    return total
