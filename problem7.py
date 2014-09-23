# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 11:34:55 2014

@author: Yusuke
"""

from sympy.ntheory import primefactors


prime_list = [2]
num_of_prime = len(prime_list)
test_num = 3
prime_flag = True

while num_of_prime < 10001:

    for prime in prime_list:
        if test_num % prime == 0:
            prime_flag = False
            break
        
    if prime_flag == True:
        prime_list.append(test_num)
        num_of_prime = len(prime_list)
    
    test_num += 1
    prime_flag = True

print prime_list, len(prime_list)

print primefactors(prime_list[-1])    
    