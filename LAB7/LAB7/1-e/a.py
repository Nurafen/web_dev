def mini(a, b, c, d):
    ls = [a,b,c,d]
    return min(ls)

a = list(map(int, input().split()))

print(mini(a[0], a[1], a[2], a[3]))