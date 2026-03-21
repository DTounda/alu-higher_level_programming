#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for element in set_1:
        for letter in set_2:
            if letter == element:
                new_set.add(element)
    return new_set
