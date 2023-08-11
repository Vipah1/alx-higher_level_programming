#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    addi = calc.add(a, b)
    subi = calc.sub(a, b)
    muli = calc.mul(a, b)
    divi = calc.div(a, b)
    print("{} + {} = {}".format(a, b, addi))
    print("{} - {} = {}".format(a, b, subi))
    print("{} * {} = {}".format(a, b, muli))
    print("{} / {} = {}".format(a, b, divi))
