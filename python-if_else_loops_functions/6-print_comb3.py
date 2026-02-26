#!/usr/bin/python3
number = 0
value = 0
while value < 10:
    number = value + 1
    while number <= 9:
        if number == 9 and value == 8:
            print("{0}{1}".format(value, number))
        else:
            print("{0}{1}".format(value, number), end=", ")
        number += 1
    value += 1
