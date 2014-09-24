# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:39:55 2014

@author: kuramoto
"""

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
    

limit = 1000000

prime_lst = generate_prime(limit)
#print prime_lst
result = []

for i_prime in prime_lst:
    str_prime = str(i_prime)
    for i in range(1, len(str_prime)):
        if int(str_prime[i:]) not in prime_lst:
            break
        
        if int(str_prime[:-i]) not in prime_lst:
            break
        
        if i == len(str_prime) - 1:
            result.append(i_prime)

print result
print sum(result)
        