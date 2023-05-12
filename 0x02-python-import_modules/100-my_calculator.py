#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import (add, sub, mul, div)

    operators = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] in operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        expr = "{} {} {}".format(a, sys.argv[2], b)
        print("{} = {}".format(expr, eval(expr)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
