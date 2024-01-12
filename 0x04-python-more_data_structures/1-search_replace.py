#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ls_new = []
    for x in my_list:
        if x == search:
            ls_new.append(replace)
        else:
            ls_new.append(x)
    return ls_new
