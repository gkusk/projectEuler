# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:16:40 2014

@author: Yusuke
"""
import math

result = []
for i in range(6 * 9**5):
    sum_num = 0
    for j_digit in str(i):
        sum_num += int(j_digit) ** 5
    
    if sum_num == i:
        print i
        result.append(i)
        
print math.fsum(result)
