# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 13:57:59 2014

@author: Yusuke
"""

filename = "problem42_input.txt"

for line in open(filename, 'r'):
        
    word_lst = line[:-1].replace('"','').split(',')

max_len = 0

for word in word_lst:
    if max_len < len(word):
        max_len = len(word)
#        print word
        
triangle_num_lst = [i * (i + 1) / 2 for i in range(int((2 * max_len * 26)**0.5) + 2) ]
#print triangle_num_lst, len(triangle_num_lst), max_len * 26

num = 0
for word in word_lst:
    ret = 0
    for i in range(len(word)):
        ret += ord(word[i]) - ord('A') + 1
    if ret in triangle_num_lst:
        num += 1        

print num