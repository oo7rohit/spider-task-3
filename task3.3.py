import math
n = int(input())
p = [1]*(n+1)
p[0] = p[1] = 0
temp = math.floor(n ** 0.5)
count = 1
for i in range(2, temp + 1):
    if p[i] == 1:
        j = i
        while i*j <= n:

            p[i*j] = 0
            j += 1
count = p.count(1)    # counting the number of prime numbers
print(count * (count + 1) * 0.5)




