#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    cal_1 = list(set_2 - set_1)
    cal_2 = list(set_1 - set_2)
    return (cal_1 + cal_2)
