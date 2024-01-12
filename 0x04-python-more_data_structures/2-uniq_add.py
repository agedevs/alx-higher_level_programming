#!/usr/bin/python3
def uniq_add(my_list=[]):
    solve = set(my_list)
    add_sum = 0
    for x in solve:
        add_sum += x
    return add_sum
