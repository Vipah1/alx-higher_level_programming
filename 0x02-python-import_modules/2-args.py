#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    if count > 1:
        print("{} arguments:".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} argguments.".format(count))
    for i in range(1, count):
        print("{}: {}".format(i, argv[i]))
