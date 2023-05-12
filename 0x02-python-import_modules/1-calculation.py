#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import (add, sub, mul, div)
    a = 10
    b = 5
    c = ["+", "-", "*", "/"]
    d = [add(a, b), sub(a, b), mul(a, b), div(a, b)]

    for i in range(len(c)):
        print("{:d} {} {:d} = {:d}".format(a, c[i], b, d[i]))
