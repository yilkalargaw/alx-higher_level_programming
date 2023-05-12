#!/usr/bin/python3
if __name__ == "__main__":
    from functools import reduce
    print(*map(lambda x: chr(x), range(65, 91)), sep='')
