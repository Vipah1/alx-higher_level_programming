#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    rep = my_list[:]
    if idx < 0:
        return my_list
    elif idx > count - 1:
        return my_list
    else:
        rep[idx] = element
        return rep[:]
