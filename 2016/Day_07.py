import re

with open('Advent_of_Code/2016/puzzle_input/07.txt') as input:
    ip_addresses = input.read().split('\n')

# Part 1:

def contains_abba(string):
    for i in range(len(string)-3):
        a, b, c, d = string[i], string[i+1], string[i+2], string[i+3]
        if a != b and a == d and b == c:
            return True


def supports_TLS(ip_address):
    if not contains_abba(ip_address):
        return False
    bracketed = re.split('\W', ip_address)[1::2]
    for x in bracketed:
        if contains_abba(x):
            return False
    return True


# Part 2:

def get_bab(string):
    bab_set = set()
    for i in range(len(string)-2):
        a, b, c = string[i], string[i+1], string[i+2]
        if a == c and a != b:
            bab_set.add(b + a + b)  
    return bab_set


def contains_bab(string, bab_set):
    for bab in bab_set:
        if bab in string:
            return True


def supports_SSL(ip_address):
    unbracketed = re.split('\W', ip_address)[::2]
    bracketed = re.split('\W', ip_address)[1::2]
    bab_set = set()
    for u in unbracketed:
        bab_set.update(get_bab(u))
    for b in bracketed:
        if contains_bab(b, bab_set):
            return True
    

part1 = sum(1 for ip in ip_addresses if supports_TLS(ip))
part2 = sum(1 for ip in ip_addresses if supports_SSL(ip))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')