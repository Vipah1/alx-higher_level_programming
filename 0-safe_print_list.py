#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t_num = 0
    try:
        while t_num < x: 
            print(my_list[i], end="")
            t_num += 1
    except IndexError:
        pass
    print()
    return t_num
