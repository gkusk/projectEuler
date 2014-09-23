# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 11:44:02 2014

@author: Yusuke
"""

def fractrial(inputnum):
    result = 1
    for i in range(1, inputnum + 1):
        result *= i
    
    return result
    
def digit_sum(inputnum):
    digit_str_lst = str(inputnum)
    sum_of_digit = 0
    for digit_dummy in digit_str_lst:
        sum_of_digit += int(digit_dummy)
        
    return sum_of_digit
    
print digit_sum(fractrial(100))
