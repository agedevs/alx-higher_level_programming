#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        cache = a_dictionary.items()
        arrange = (sorted(cache, key=lambda item: item[1], reverse=True))
        return arrange[0][0]
