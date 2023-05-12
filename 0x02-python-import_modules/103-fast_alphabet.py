#!/usr/bin/python3
if __name__ == "__main__":
    from functools import reduce
    print(reduce(lambda x, y: x + y, map(lambda x: chr(x), range(65, 91))))
