#!/usr/bin/python3
def no_c(my_string):
    count = len(my_sring)
    not_c = 'cC'
    new_str = list(my_string)
    for i in range(count):
        if new_str[i] in not_c:
            new_str[i] = ""
    return "".join(new_string)
