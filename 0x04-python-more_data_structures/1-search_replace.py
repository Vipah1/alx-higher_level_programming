#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newL = []
    for i in my_list:
        if i == search:
            i = replace
            newL.append(i)
    return newL
