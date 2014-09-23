# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 17:18:31 2014

@author: Yusuke
"""

from sympy import factorint

low_limit = 1
up_limit = 100000

def triangular_num(index):
    result = index * (index + 1) / 2    
    return result

def divisors_num(lst):
    result = 1    
    for divisor_dummy in lst:
        result *= (divisor_dummy + 1)
    
    return result - 1
    
for test_index in range(low_limit, up_limit):
    test_num = triangular_num(test_index)    
    prime_dic = factorint(test_num)    
    num_of_divisors = divisors_num(prime_dic.values())    
    print num_of_divisors
    if num_of_divisors > 500:
        print test_num, test_index, prime_dic, num_of_divisors
        break
    
