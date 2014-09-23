# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 15:23:46 2014

@author: Yusuke
"""

def readfile(filename, lst):
    for line in open(filename, 'r'):
        lst.append(line[:-1].split(' '))
        
def up_product(lst, outlst, adjacent_num):
    for start_raw in range(len(lst) - adjacent_num):
        for start_col in range(len(lst)):
            lst_dummy = []
            for num_dummy in range(adjacent_num):
                lst_dummy.append(int(lst[start_raw + num_dummy][start_col]))
            outlst.append(lst_dummy)
            
def vertical_product(lst, outlst, adjacent_num):
    for start_raw in range(len(lst)):
        for start_col in range(len(lst) - adjacent_num):
            lst_dummy = []
            for num_dummy in range(adjacent_num):
                lst_dummy.append(int(lst[start_raw][start_col + num_dummy]))
            outlst.append(lst_dummy)
                
def right_down_diagonal_product(lst, outlst, adjacent_num):
    for start_raw in range(len(lst) - adjacent_num):
        for start_col in range(len(lst) - adjacent_num):
            lst_dummy = []
            for num_dummy in range(adjacent_num):
                lst_dummy.append(int(lst[start_raw + num_dummy][start_col + num_dummy]))
            outlst.append(lst_dummy)

    
def right_up_diagonal_product(lst, outlst, adjacent_num):
    for start_raw in range(adjacent_num - 1, len(lst)):
        for start_col in range(len(lst) - adjacent_num):
            lst_dummy = []    
            for num_dummy in range(adjacent_num):
                lst_dummy.append(int(lst[start_raw - num_dummy][start_col + num_dummy]))
            outlst.append(lst_dummy)

def product(value_pair_lst):
    for value_pair in value_pair_lst:
        result = 1
        for value_dummy in value_pair:
            result *= value_dummy
            yield result

filename = 'problem11_input.txt'
input_lst = []
output_lst = []
readfile(filename, input_lst)
max_product = 1
adjacent_num = 4

up_product(input_lst, output_lst, adjacent_num)
vertical_product(input_lst, output_lst, adjacent_num)
right_down_diagonal_product(input_lst, output_lst, adjacent_num)
right_up_diagonal_product(input_lst, output_lst, adjacent_num)

print max(product(output_lst))


        