#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    for i in range(0, count):
        c_sum += int(argv[i])
    print("{}".format(c_sum))
