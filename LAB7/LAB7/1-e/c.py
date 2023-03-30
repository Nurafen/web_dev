def xor(x, y):
    if x != y:
        return True
    else:
        return False


a = input().split()

if xor(a[0], a[1]):
    print(1)
else:
    print(0)