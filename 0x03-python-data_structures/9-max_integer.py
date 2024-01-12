#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the largest integer of this list."""
    if len(my_list) == 0:
        return (None)
    srt_large = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > srt_large:
            srt_large = my_list[i]

    return (srt_large)
