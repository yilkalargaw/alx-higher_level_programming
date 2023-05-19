#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list(map(lambda key: a_dictionary.pop(key),
             [i for i in a_dictionary if a_dictionary[i] == value]))
    return a_dictionary
