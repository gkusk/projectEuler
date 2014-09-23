# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 13:39:20 2014

@author: Yusuke
"""

"""
中央からn個目の辺の長さ = 2n + 1
中央からn個目の正方形に含まれる個数 = n**2

右上対角数列： an = (2n + 1)**2
左上対角数列： an = (2n + 1)**2 - 2n
左下対角数列： an = (2n + 1)**2 - 2n*2 
右下対角数列： an = (2n + 1)**2 - 2n*3
"""

result = 0
for i in range(1, 501):
    result += 4 * (2 * i + 1)**2 - 2 * i * (1 + 2 + 3)

print result + 1   


