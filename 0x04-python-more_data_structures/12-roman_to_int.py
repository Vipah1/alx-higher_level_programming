#!/usr/bin/python3
def roman_to_int(roman_string):
    rmn_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rmn_list = list(roman_string)
    result = 0
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    else:
        for i in rmn_list:
            if i in rmn_nums:
                result += rmn_nums[i]
        return result
