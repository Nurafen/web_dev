# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dt = {}
dist_cnt = 0

for i in range(n):
    x = input()
    if x in dt.keys():
        dt[x] += 1
    else:
        dist_cnt += 1
        dt[x] = 1

print(dist_cnt)
print(*dt.values())

# print(*dt.values())