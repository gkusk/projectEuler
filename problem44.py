# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 00:13:00 2014

@author: Yusuke
"""

def pentagonal(num):
    return num * (3 * num - 1) / 2
    
limit = 10000

lst = [pentagonal(i) for i in range(1,limit)]

for j in range(1000):
    diff_lst = [lst[i+j] - lst[i] for i in range(len(lst) - j) ]
    sum_lst  = [lst[i+j] + lst[i] for i in range(len(lst) - j) ]
    for i in range(len(diff_lst)):
        if (diff_lst[i] in lst)  and (sum_lst[i] in lst):
            print diff_lst[i], sum_lst[i], lst[i], lst[j]

