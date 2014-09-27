# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:15:01 2014

@author: Yusuke
"""

def permutation(lst, num):
    if len(lst) <= 1:
        return [lst]
    if len(lst) >= 2 and num != 0:
        result = []
        for i in range(len(lst)):
            result.extend( [lst[i]] + x for x in permutation(lst[:i]+lst[i+1:], num -1))
        return result

    if num == 0:
        return [[]]

def list_to_number(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]*10**(len(lst) - 1 - i)
    
    return result
    
def number_to_list(num):
    ret_lst = []
    while num % 10 != num:
        ret_lst.append(num % 10)
        num //= 10

    ret_lst.append(num)
    return ret_lst[::-1]
    

a = range(9, 0, -1)
check_lst = permutation(a, 4)

for base_dummy in check_lst:
    base_4digit_1st = list_to_number(base_dummy)
    base_4digit_2nd = base_4digit_1st * 2
    num_list = base_dummy + number_to_list(base_4digit_2nd)
    if set(a) == set(num_list):
        print base_4digit_1st, base_4digit_2nd

