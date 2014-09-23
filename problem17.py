# -*- coding: utf-8 -*-
"""
Created on Sun Sep 07 11:18:16 2014

@author: Yusuke
"""

one_ten = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
eleven_twenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_hundred = ['twenty', 'thirty', 'fourty', 'fifty', 'sixth', 'seventy', 'eighty', 'ninety', 'hundred']

def digit_list(input_num):
    return [int(input_num / 1), int(input_num / 10), int(input_num / 100)]
    

def call_num_of_one_ten(lst):
    return lst[2] * 9 + 