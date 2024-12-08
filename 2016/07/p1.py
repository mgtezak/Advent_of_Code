import re


def part1(puzzle_input):

    def contains_abba(string):
        for i in range(len(string)-3):
            a, b, c, d = string[i], string[i+1], string[i+2], string[i+3]
            if a != b and a == d and b == c:
                return True

    def supports_TLS(ip_address):
        if not contains_abba(ip_address):
            return False
        bracketed = re.split(r'\W', ip_address)[1::2]
        for x in bracketed:
            if contains_abba(x):
                return False
        return True

    return sum(supports_TLS(ip) for ip in puzzle_input.split('\n'))