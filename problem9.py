# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 12:45:21 2014

@author: Yusuke
"""

for a in range(1,1000):
    for b in range(2,1000):
        if (1000 - a - b)**2 - a**2 - b **2 == 0:
            print a, b, 1000 - a - b
            print a * b * (1000 - a - b)
            print (1000 -a), (1000 -b)
            

