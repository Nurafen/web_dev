import math

n = int(input())
i = 1

while i <= n:
    if math.sqrt(i).is_integer():
        print(i)
    i += 1
