# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 17:22:19 2014

@author: Yusuke
"""

def readfile(filename):
    for line in open(filename, 'r'):
        yield int(line[:-1])

filename = 'problem13_input.txt'        
print sum(readfile(filename))
