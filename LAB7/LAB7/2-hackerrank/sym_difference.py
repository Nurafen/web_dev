# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

st1 = set(map(int, input().split()))

m = int(input())

st2 = set(map(int, input().split()))

st = list(st1.symmetric_difference(st2))
st.sort()

for i in st:
    print(i)