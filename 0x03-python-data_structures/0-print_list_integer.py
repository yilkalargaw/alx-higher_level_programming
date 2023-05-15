#!/usr/bin/python3
def print_list_integer(my_list=[]):
    print(*list(map(lambda x: "{:d}".format(x), my_list)), sep='\n')
