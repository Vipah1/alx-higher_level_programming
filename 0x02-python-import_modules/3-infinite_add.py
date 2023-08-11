#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(agrv)
    summ = 0
    for i in range(1, count):
        summ += int(argv[i])
    print("{}".format(summ))
