n = int(input())

ls = list(map(int, input().split()))

for i in range(n // 2):
    ls[i], ls[n - 1 - i] = ls[n - 1 - i], ls[i]

print(*ls)