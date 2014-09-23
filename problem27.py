# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 16:18:53 2014

@author: Yusuke
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

limit = 100000
prime_lst = generate_prime(limit)
print prime_lst


#a, bの組み合わせ
a_lst = []
b_lst = []

for b_prime in prime_lst:
    if b_prime > 1000:
        break
    for first_prime in prime_lst:
        a = first_prime - 1 - b_prime
        if a > 1000 or a < -1000: 
            break
        a_lst.append(a)
        b_lst.append(b_prime)

#素数列生成長さの探索
check_length = 1000
len_lst = []
for i in range(len(a_lst)):
    for n in range(2, check_length):
        prime_candidate = n**2 + a_lst[i]*n + b_lst[i]
        
        if prime_candidate not in prime_lst:
            len_lst.append(n)
            if prime_candidate > prime_lst[-1]:
                print "need more prime list"
            
            break
         
        if n == check_length - 1:
            len_lst.append(n)
            print "more check length"
            
print max(len_lst), len_lst.index(max(len_lst)), len_lst[37427]
print a_lst[37427], b_lst[37427], a_lst[37427] * b_lst[37427]
