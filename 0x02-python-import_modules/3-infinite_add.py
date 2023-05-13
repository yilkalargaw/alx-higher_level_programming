#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print((lambda args: sum(int(i) for i in args))(sys.argv[1:]))
