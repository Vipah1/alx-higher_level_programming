#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    c_sum = 0
    for i in range(count):
        c_sum += int(argv[i])
    print("{}".format(c_sum))
