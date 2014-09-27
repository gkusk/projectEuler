# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 11:34:49 2014

@author: Yusuke
"""
from sympy.ntheory import primefactors

def accumurate_sum(num):
    ret = 0
    for i in range(num + 1):
        ret += i
       
    return ret
    
for i in range(1,10):
    print accumurate_sum(i), i

def generate_prime(n):
    primes = []
    numlist = list(range(0, n))
    for i in range(2, n):
        if numlist[i] > 0:
            j = i*2
            while j < n:
                numlist[j] = 0
                j += i
    for i in range(2, n):
        if numlist[i] > 0:
            primes.append(i)
    return primes

def permutation(lst, num):
    if len(lst) <= 1:
        return [lst]
    if len(lst) >= 2 and num > 1:
        result = []
        for i in range(len(lst)):
            result.extend([ lst[i] ] + x for x in permutation(lst[:i] + lst[i+1:], num -1 ) )
        return result
    if num == 1:
        return result

def make_odd_lst(input_lst):
    result = []
    for test_lst in input_lst:
        if test_lst[len(test_lst) - 1] % 2 == 1:
            result.append(test_lst)
    return result

def lst_to_num(input_lst):
    ret = 0    
    for i in range(len(input_lst)):
        ret += input_lst[i] * 10 ** (len(input_lst) - 1 - i)
    return ret

input_num_lst = range(7, 0, -1)
test_lst = make_odd_lst(permutation(input_num_lst, 7))
"""
print test_lst[0]
print lst_to_num(test_lst[0])
"""
for i in test_lst:
    test_num = lst_to_num(i)
    if len(primefactors(test_num)) == 1:
        print test_num
        break
