#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    nums = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))

    if isinstance(roman_string, str) and all(i in nums for i in roman_string):
        return reduce(lambda x, y: x + y if x >= y else x - y,
                      [nums.get(i, 0) for i in roman_string])
    return 0
