# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 22:19:54 2014

@author: Yusuke
"""
from sympy import factorint

def check_fraction(num1, num2):
    frac = float(num1)/float(num2)
    if frac < 1:
        if str(num2)[0] != "0" and ( str(num1)[0] != "0" and str(num1)[1] != "0"):
            if float(str(num1)[0]) / float(str(num2)[0]) == frac and str(num1)[1] == str(num2)[1]:
                return True
            if float(str(num1)[1]) / float(str(num2)[0]) == frac and str(num1)[0] == str(num2)[1]:
                return True
    
        if str(num2)[1] != "0" and (str(num1)[0] != "0" and str(num1)[1] != "0"):
            if float(str(num1)[0]) / float(str(num2)[1]) == frac and str(num1)[1] == str(num2)[0]:
                return True
            if float(str(num1)[1]) / float(str(num2)[1]) == frac and str(num1)[0] == str(num2)[0]:
                return True
            
product = []
for i in range(10, 100):
    for j in range(i, 100):
        if check_fraction(i, j):
            product.append([i, j])
            
print product

prime_dict = {}

for pair_num in product:
    first_dict = factorint(pair_num[0])
    second_dict = factorint(pair_num[1])
    
    for key, val in first_dict.items():
        if not prime_dict.has_key(key):
            prime_dict[key] = 0
            
        prime_dict[key] += val
        #print key, val

    for key, val in second_dict.items():
        if not prime_dict.has_key(key):
            prime_dict[key] = 0
        prime_dict[key] += -val
        #print key, val
print prime_dict

result = 1
for key, val in prime_dict.items():
    if val < 0:
        result *= key ** (-val)

print result