#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for uniq_key in sorted(a_dictionary):
        print("{}: {}".format(uniq_key, a_dictionary[unig_key]))
