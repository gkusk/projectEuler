# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 14:34:32 2014

@author: Yusuke
"""

def permutation(lst, num):
    if len(lst) <= 1:
        return [lst]
    elif len(lst) >= 2 and num > 1:
        result = []
        for i in range(len(lst)):
            result.extend([ lst[i] ] + x for x in permutation(lst[:i] + lst[i+1:], num - 1))
        return result
    elif num == 1:
        return result

def lst_to_num(lst):
    ret = 0
    for i in range(len(lst)):
        ret += lst[i] * 10 **(len(lst) - 1 - i)
    return ret

def check_2(num):
    if lst_to_num([int(x) for x in str(num)[1:4] ]) % 2 == 0:
        return True

def check_3(num):
    if lst_to_num([int(x) for x in str(num)[2:5] ]) % 3 == 0:
        return True

def check_4(num):
    if lst_to_num([int(x) for x in str(num)[3:6] ]) % 5 == 0:
        return True

def check_5(num):
    if lst_to_num([int(x) for x in str(num)[4:7] ]) % 7 == 0:
        return True

def check_6(num):
    if lst_to_num([int(x) for x in str(num)[5:8] ]) % 11 == 0:
        return True

def check_7(num):
    if lst_to_num([int(x) for x in str(num)[6:9] ]) % 13 == 0:
        return True

def check_8(num):
    if lst_to_num([int(x) for x in str(num)[7:10] ]) % 17 == 0:
        return True
    
num_list = range(10)

d3_to_d10_lst = []
for d4 in range(0,10,2):
    for d6 in set([0,5]).difference([d4]):
        for d5 in set(num_list).difference([d4, d6]):
            for d3 in set(num_list).difference([d4, d5, d6]):
                if (d3 + d4 +d5) % 3 == 0:
                    for d7 in set(num_list).difference([d3, d4, d6, d5]):
                        if (100*d5 + 10*d6 + d7) % 7 == 0:
                            for d8 in set(num_list).difference([d3, d4, d6, d5, d7]):
                                if (100*d6 + 10*d7 + d8) % 11 == 0:
                                    for d9 in set(num_list).difference([d3, d4, d6, d5, d7, d8]):
                                        for d10 in set(num_list).difference([d3, d4, d6, d5, d7, d8, d9]):
                                            if (100*d7 + 10*d8 + d9) % 13 == 0 and (100*d8 + 10*d9 + d10) % 17 == 0:
                                                d3_to_d10_lst.append([d3, d4, d5, d6, d7, d8, d9, d10])

#print d3_to_d10_lst
result_lst = []
for i in range(len(d3_to_d10_lst)):
    for d1 in set(num_list).difference(d3_to_d10_lst[i]):
        if d1 != 0:
            for d2 in set(num_list).difference(d3_to_d10_lst[i] + [d1]):
                result_lst.append([d1, d2] + d3_to_d10_lst[i])

#print result_lst


result_sum = 0
for i in result_lst:
    result_sum += lst_to_num(i)
    ret = lst_to_num(i)    
    print check_2(ret), check_3(ret), check_4(ret), check_5(ret), check_6(ret), check_7(ret), check_8(ret)
    print ret    
    
print result_sum