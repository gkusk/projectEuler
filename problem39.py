# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 10:22:10 2014

@author: Yusuke
"""

import math

def is_square(num):
    if num > 0:
        if num == int(math.sqrt(num))**2:
            return True
        else:
            return False
    else:
        return False

max_pair_num = 0

for p in range(1000, 4, -1):
    low_limit = int(p * (math.sqrt(2) - 1))
    up_limit = int(p/2) + 1
    
    if up_limit - low_limit < max_pair_num:
        break
    
    test_pair_num = 0
    for c in range(low_limit, up_limit):
        D = 2*c**2 - (p-c)**2    
        if is_square(D):
            b = (p - c - int(D**0.5))/2
            if b % 2 == 0 and b > 0:
                # = (p - c + int(D**0.5))/2
                test_pair_num += 1
    
    if test_pair_num > max_pair_num:
        max_pair_num = test_pair_num
        max_p = p

print max_p, max_pair_num
    
    