#!/usr/bin/python3
def fizzbuzz():
    number = 0
    while number < 101:
        number += 1 
        if number % 15 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
    
