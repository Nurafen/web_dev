a = int(input())

if a == 1:
    cnt = 1
else:
    cnt = 2
    for i in range(2, a):
        if a % i == 0:
            cnt += 1

print(cnt)