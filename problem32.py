# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 21:53:12 2014

@author: Yusuke
"""

num_list = range(1,10)

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
        

def first_case_check(num_lst):
    a = num_lst[0]
    b = num_lst[1]*1000 + num_lst[2] * 100 + num_lst[3] * 10 + num_lst[4]
    c = num_lst[5]*1000 + num_lst[6] * 100 + num_lst[7] * 10 + num_lst[8]
    
    if c == a * b:
        return c
    else:
        return 0
        
def second_case_check(num_lst):
    a = num_lst[0] * 10 + num_lst[1] 
    b = num_lst[2] * 100 + num_lst[3] * 10 + num_lst[4]
    c = num_lst[5] *1000 + num_lst[6] * 100 + num_lst[7] * 10 + num_lst[8]
    
    if c == a * b:
        return c
    else:
        return 0

product_lst = []
for i in permutations(num_list, 10):
    ret1 = first_case_check(i)
    ret2 = second_case_check(i)     
    if ret1 > 0 or ret2 > 0:
        product_lst.append(ret1)
        product_lst.append(ret2)

        
print sum(set(product_lst))