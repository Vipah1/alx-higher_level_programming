#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    addi = add(a, b)
    subi = sub(a, b)
    muli = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, addi))
    print("{} - {} = {}".format(a, b, subi))
    print("{} * {} = {}".format(a, b, muli))
    print("{} / {} = {}".format(a, b, divi))
