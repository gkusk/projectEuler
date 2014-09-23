# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 13:06:37 2014

@author: Yusuke
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 11:34:55 2014

@author: Yusuke
"""

limit = 2000000

crosslimit = limit ** 0.5
candidate_list = range(limit)

for test_num in range(4, limit, 2):
    candidate_list.remove(test_num)

test_index = 3
while test_index < len(candidate_list):
    test_num = candidate_list[test_index]
    for del_num in range( test_num ** 2, limit, 2*test_num):
        if del_num in candidate_list:
            candidate_list.remove(del_num)
    
    test_index += 1    
    
print candidate_list, sum(candidate_list)
    