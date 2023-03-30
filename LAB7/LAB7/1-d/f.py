n = int(input())
ls = list(map(int, input().split()))
s = 0

for i in range(1, n - 1):
    if ls[i - 1] < ls[i] and ls[i + 1] < ls[i]:
        s += 1

print(s)