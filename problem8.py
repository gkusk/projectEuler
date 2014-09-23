# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 11:55:46 2014

@author: Yusuke
"""

lst = []
for line in open('problem8_input.txt', 'r'):
    lst.extend(line[:-1])
    

search_num = 13
maxnum = 0
num_product = 1
    
for i in range(len(lst) - search_num):
    num_product = 1
    for k in range(search_num):
        num_product *= int(lst[i + k])
        if num_product == 0:
            break
    
    if maxnum < num_product:
        maxnum = num_product
    
print maxnum    
