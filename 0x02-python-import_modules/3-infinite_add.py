#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    for i in range(0, count):
        c_sum = i + int(argv[i])
        i += 1
    print("{}".format(c_sum))
