n = int(input())
ls = list(map(int, input().split()))
s = 0

for i in range(n - 1):
    if (ls[i] > 0 and ls[i + 1] > 0) or (ls[i] < 0 and ls[i + 1] < 0):
        s += 1
        break

if s == 0:
    print("NO")
else:
    print("YES")