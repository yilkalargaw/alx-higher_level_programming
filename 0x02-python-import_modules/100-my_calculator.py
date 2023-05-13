#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import (add, sub, mul, div)

    operators = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    try:
        int(sys.argv[1])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    try:
        int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] in operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        expr = "{} {} {}".format(a, sys.argv[2], b)
        if sys.argv[2] == "/":
            result = a // b
        else:
            result = eval(expr)
        print("{} = {}".format(expr, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
