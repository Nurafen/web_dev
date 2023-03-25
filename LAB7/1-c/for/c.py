
import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    c =  math.sqrt(i)
    if c.is_integer():
        print(i, end=' ')