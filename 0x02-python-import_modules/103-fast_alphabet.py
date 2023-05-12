#!/usr/bin/python3
if __name__ == "__main__":
    print(*map(lambda x: chr(ord('A') + x), range(26)), sep='')
