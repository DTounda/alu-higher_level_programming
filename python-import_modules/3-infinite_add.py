#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = argv[1:]
    total_sum = sum(map(int, count))
    print(total_sum)
