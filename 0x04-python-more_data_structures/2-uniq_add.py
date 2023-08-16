#!/usr/bin/python3
def uniq_add(my_list=[]):
    cnt = set(my_list)
    sum = 0
    for i in cnt:
        sum += i

    return sum
