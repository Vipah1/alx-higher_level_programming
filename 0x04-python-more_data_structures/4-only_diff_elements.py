#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    o_diff = set()
    
    for i in set_1:
        if i not in set_2:
            o_diff.add(i)

    for i in set_2 and not in o_diff:
        if i not in set_1:
            o_diff.add(i)
    
    return o_diff
