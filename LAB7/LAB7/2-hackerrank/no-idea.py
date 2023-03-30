# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input().split()

ar = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0

for el in ar:
    if el in a:
        happiness += 1
    elif el in b:
        happiness -= 1

print(happiness)