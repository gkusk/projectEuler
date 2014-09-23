sum = 0
input = 1000

for i in range(input):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print sum 