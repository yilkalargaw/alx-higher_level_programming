#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))

    if isinstance(roman_string, str) and all(i in nums for i in roman_string):
        equivalents = [nums.get(i, 0) for i in roman_string]
        return sum(map(lambda x: -x[0] if x[0] < x[1] else x[0],
                   zip(equivalents, equivalents[1:] + [0])))

    return 0
