import re


def part2(puzzle_input):

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
        unbracketed = re.split(r'\W', ip_address)[::2]
        bracketed = re.split(r'\W', ip_address)[1::2]
        bab_set = set()
        for u in unbracketed:
            bab_set.update(get_bab(u))
        for b in bracketed:
            if contains_bab(b, bab_set):
                return True
        return False
        
    return sum(supports_SSL(ip) for ip in puzzle_input.split('\n'))