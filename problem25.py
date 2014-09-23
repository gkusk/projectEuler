# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 08:37:42 2014

@author: Yusuke
"""

limit_num = 10000
fn = 1
fn_1 = 1

for i in range(limit_num):
    fn_2 = fn + fn_1
    if len(str(fn_2)) == 1000:
        print fn_2
        print i + 3
        break
    
    fn = fn_1
    fn_1 = fn_2
    