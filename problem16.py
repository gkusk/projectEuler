# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 11:10:39 2014

@author: Yusuke
"""

sum_digit = 0
for i in str(2**1000):
    sum_digit += int(i)

print sum_digit