# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:36:39 2014

@author: Yusuke
"""

def coin_sums(coin_lst, target):
    if coin_lst == []:
        return [[]]
    if len(coin_lst) > 1 and target > 0:
        result = []
        for coin_index in range(len(coin_lst)):
            if target >= coin_lst[coin_index]:
                result.extend([coin_lst[coin_index]] 
                    + x for x in coin_sums(coin_lst[coin_index:], target - coin_lst[coin_index]))
        return result

    if target == 0:
        return [[]]

coin_lst = [1, 2, 5, 10, 20, 50, 100, 200]
print len(coin_sums(coin_lst, 200))

print 