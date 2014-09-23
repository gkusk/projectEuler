# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 14:01:15 2014

@author: Yusuke
"""

num_lst = []
for a in range(2, 101):
    for b in range(2, 101):
        num_lst.append(a**b)
        
print len(sorted(set(num_lst), key=num_lst.index))

