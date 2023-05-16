#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        print(*list(map(lambda x: "{:d}".format(x), my_list[::-1])), sep='\n')
