# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 10:25:05 2014

@author: Yusuke
"""

prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
prime_index_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def check_trianglar_number(test_num):
    n = int((-1 + (1 + 8 * test_num) **0.5 ) / 2)
    if test_num - n * (n + 1)/2 == 0:
        return True
        
