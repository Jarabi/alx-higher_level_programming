#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    my_set = set(my_list)
    uniq_sum = sum(list(my_set))
    return (uniq_sum)
