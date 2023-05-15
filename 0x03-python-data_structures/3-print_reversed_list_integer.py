def print_reversed_list_integer(my_list=[]):
    print(*list(map(lambda x: "{:d}".format(x), my_list[::-1])), sep='\n')
