#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or (not (idx in range(len(my_list)))):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                del my_list[i]
                return my_list
