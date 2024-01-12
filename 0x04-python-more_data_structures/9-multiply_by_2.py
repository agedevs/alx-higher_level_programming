#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    testdict = a_dictionary.copy()
    for key in testdict.keys():
        testdict[key] = a_dictionary[key] * 2
    return testdict
