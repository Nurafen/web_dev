n = int(input())
ls = list(map(int, input().split()))

for i in range(0, n, 2):
    print(ls[i], end=' ')