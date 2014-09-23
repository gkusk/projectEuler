# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 11:05:14 2014

@author: Yusuke
"""

def fractrial(index):
    result = 1    
    for i in range(1, index + 1):
        result *= i
    return result

def lattice_path(index):
    return fractrial(2 * index) / fractrial(index) ** 2
    
print lattice_path(20)
    