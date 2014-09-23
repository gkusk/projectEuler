# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 00:28:16 2014

@author: Yusuke
"""

from sympy.ntheory import primefactors


for i in range(9,0,-1):
    for j in range(9,-1,-1):
        input_number = i * 1e3 + j * 1e2 + j * 1e1 + i
        prime_lst = primefactors(input_number)            
        max_prime = max(prime_lst)            
        if max_prime < 100:
            print input_number, prime_lst
                
"""
for i in range(9,0,-1):
    for j in range(9,-1,-1):
        for k in range(9,-1,-1):
            input_number = i * 1e5 + j * 1e4 + k * 1e3 + k * 1e2 + j * 1e1 + i
            prime_lst = primefactors(input_number)            
            max_prime = max(prime_lst)            
            if max_prime < 100:
                print input_number, prime_lst
"""                
            
            
        