n = int(input())
degree = 1
cnt = 0

while degree < n:
    degree *= 2
    cnt += 1

print(cnt)