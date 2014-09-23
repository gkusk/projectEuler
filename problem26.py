# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 15:03:04 2014

@author: Yusuke
1/xが循環小数とする
xの桁数i
オフセットj
循環桁数k

例：0.01234(5678) -> i = 2, j = 4, k = 4

とすると次の関係式が成り立つ

10^(i + j) * ( 10^k - 1) = x * y (ここでｙは整数)

xに含まれる約数から10^(i + j)の約数を除いた分が10^k - 1で補われる。
従って、1-1000までに含まれる素数で1000までに許される指数分を10^k-1で補う時の最小のkを各素数に対して計算し
その中から最大のkを選べばよい

"""
import math

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

prime_list = generate_prime(1000)
index_lst = []

for i_prime in range(len(prime_list)):
    index_lst.append(int( 3 / math.log10(prime_list[i_prime]) ))

length_lst = [0 for i in range(len(prime_list))]
limit = 1000

for i_prime in range(len(prime_list)):
    for i_length in range(1,limit):
        if ( 10**i_length - 1 ) % ( prime_list[i_prime]**index_lst[i_prime] ) == 0:
            length_lst[i_prime] = i_length
            break
        elif i_length == limit - 1:
            length_lst[i_prime] = 0
        

print length_lst
print prime_list
print max(length_lst), prime_list[length_lst.index(max(length_lst))]


