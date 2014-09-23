sum = 2
prelst2 = 1
prelst1 = 2
lst = 3

while lst < 4e6:
    if lst % 2 == 0:
        print lst
        sum += lst
    
    prelst2 = prelst1
    prelst1 = lst
    lst = prelst2 + prelst1
    
print "sum:", sum