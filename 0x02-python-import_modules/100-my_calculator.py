#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    op_list = "+-*/"
    a = int(argv[0])
    b = int(argv[4])
    op = argv[2]
    count = len(agrv)
    ans = 0
    if count != 4:
        print("Usage: ./100-my_calculator.py {} {} {}".format(a, op, b))
        exit(1)
    if op not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    for op in op_list:
        if op = "+":
            ans = a + b
            print("{} + {} = {}".format(a, b, ans))
        elif op = "-":
            ans = a - b
            print("{} - {} = {}".format(a, b, ans))
        elif op = "*":
            ans = a * b
            print("{} * {} = {}".format(a, b, ans))
        else:
            ans = a / b
            print("{} / {} = {}".format(a, b, ans))
