n = int(input())
ls = list(map(int, input().split()))
s = 0

for i in range(n):
    if ls[i] > 0:
        s += 1

print(s)