# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:29:20 2014

@author: kuramoto
"""

limit = 1000000
result = []
for i in range(limit):
    if str(i) == str(i)[::-1]:
        if format(i, 'b') == format(i, 'b')[::-1]:
            result.append(i)

print result
print sum(result)

