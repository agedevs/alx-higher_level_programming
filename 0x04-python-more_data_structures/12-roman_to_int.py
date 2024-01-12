#!/usr/bin/python3
def roman_to_int(roman_string):
    add_num = 0
    end_count = 0
    count = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0

    for c in reversed(roman_string):
        for elem in count:
            if c == elem[0]:
                if elem[1] < end_count:
                    add_num -= elem[1]
                else:
                    add_num += elem[1]
                end_count = elem[1]
    return add_num
