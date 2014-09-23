# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 14:14:08 2014

@author: Yusuke
"""
import  math

def permutations(L, num):
    if L == []:
        return [[]]
    elif len(L) == 1:
        return [L]
    elif len(L) >= 2 and num > 1:
        result = []
        for i in range(1, len(L) + 1):
            result.extend([L[i-1]] + x
                for x in permutations(L[0:i-1]+L[i:], num - 1))
        return result
    elif num == 1:
        return [[]]


num_of_each = [4, 4, 4, 4, 5, 5, 5, 3, 1]
num_lst = []

for i in range(len(num_of_each)):
    print i
    for j in range(num_of_each[i]):
        num_lst.append(i)
        
print len(num_lst)
print permutations(num_lst, 5)
