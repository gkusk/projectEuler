# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 10:36:37 2014

@author: Yusuke
"""

total_first_month = 12 * 100
day_start = 366 % 7 

total_sunday_on_first_month = (total_first_month + day_start) // 7
print total_sunday_on_first_month
