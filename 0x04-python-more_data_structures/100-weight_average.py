#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    add_a = 0
    add_b = 0
    for elem in my_list:
        add_a += (elem[0] * elem[1])
        add_b += elem[1]
    return add_a / add_b
