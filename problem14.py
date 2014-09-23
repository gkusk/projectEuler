# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 10:44:05 2014

@author: Yusuke
"""

limit = 1000000
max_seq = 1
max_seq_input = 1

for start_test_num in range(limit, 1, -1):
    seq = 0    
    test_num = start_test_num    
    while test_num > 2:   
        seq += 1
        if test_num % 2 == 0:
            test_num /= 2
        else:
            test_num = 3 * test_num + 1
            
    if max_seq < seq:
        max_seq = seq
        max_seq_input = start_test_num
        
print max_seq, max_seq_input
