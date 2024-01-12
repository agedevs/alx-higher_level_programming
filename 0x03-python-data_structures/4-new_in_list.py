#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count_len = len(my_list) - 1
    if (idx < 0 or idx > count_len):
        return (my_list)
    else:
        my_new_list = my_list[:]
        my_new_list[idx] = element
        return (my_new_list)
