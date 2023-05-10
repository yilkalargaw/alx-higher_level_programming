#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        change = 32 if (ord(c) >= 97 and ord(c) <= 122) else 0:
            print("{:c}".format(ord(str[i]) - 32), end="")
    print("")
