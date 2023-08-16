#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newL = []
    if my_list:
        for i in my_list:
            if i == search:
                i = replace
                newL.append(i)
            else:
                newL.append(i)
        return newL
    else:
        return my_list
