#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mulby2 = []
    for index in my_list:
        if index % 2 == 0:
            mulby2.append(True)
        else:
            mulby2.append(False)

    return mulby2
