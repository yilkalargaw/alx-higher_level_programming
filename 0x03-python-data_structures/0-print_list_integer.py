#!/usr/bin/python3
def print_list_integer(my_list=[]):
    (lambda lst: print(*lst, sep='\n'))(my_list)
