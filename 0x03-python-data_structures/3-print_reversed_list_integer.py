#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list==None or len(my_list) == 0:
        print("")
    else:
        print(*list(map(lambda x: "{:d}".format(x), my_list[::-1])), sep='\n')
