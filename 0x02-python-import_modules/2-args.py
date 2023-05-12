#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv[1:])
    if length == 0:
        suffix = "s."
    elif length == 1:
        suffix = ":"
    else:
        suffix = "s:"

    print("{:d} argument{}".format(length, suffix))

    for i in range(length):
        print("{:d}: {}".format(i+1, sys.argv[i+1]))
