#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:c}".format(ord(str[i]) - 32),
                  end="\n" if (i == (len(str) - 1)) else "")
        else:
            print("{:c}".format(ord(str[i])),
                  end="\n" if (i == (len(str) - 1)) else "")
            

uppercase("Best")
uppercase("best")
uppercase("MclcaC")
uppercase("cMca")
