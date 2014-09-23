# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 23:03:43 2014

@author: Yusuke
"""

def fractrial(num):
    result = 1    
    if num == 1 or num == 0:
        return result
    if num > 1:
        result = num * fractrial(num-1)
        return result

frac_lst = []        
for i in range(0,10):
    frac_lst.append(fractrial(i))

num_lst = []
for i in range(0, frac_lst[-1] * 6):
    result = 0    
    for j in str(i):
        result += frac_lst[int(j)]
    
    if result == i:
        num_lst.append(i)

print num_lst
print sum(num_lst) - 3