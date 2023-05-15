#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_list = []

    if (len(my_list) == 0):
        return even_list

    for i in my_list:
        if (i % 2 == 0):
            even_list.append(True)
        else:
            even_list.append(False)

    return even_list
