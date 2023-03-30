n = int(input())
okay = False
degree = 1

while degree <= n:
    if degree == n:
        print("YES")
        okay = True
        break
    degree *= 2

if not okay:
    print("NO")