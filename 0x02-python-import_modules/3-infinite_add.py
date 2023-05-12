#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    j = lambda args: sum(int(i) for i in args)

    print(j(sys.argv[1:]))
