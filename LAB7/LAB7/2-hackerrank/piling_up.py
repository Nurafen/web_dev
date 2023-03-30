# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for test in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    stack = []
    possible = "Yes"

    for i in range(n):
        if ls[0] >= ls[len(ls) - 1]:
            if len(stack) == 0:
                stack.append(ls[0])
                ls.pop(0)
            else:
                if stack[len(stack) - 1] >= ls[0]:
                    stack.append(ls[0])
                    ls.pop(0)
                else:
                    possible = "No"
                    break
        else:
            if len(stack) == 0:
                stack.append(ls[len(ls) - 1])
                ls.pop()
            else:
                if stack[len(stack) - 1] >= ls[len(ls) - 1]:
                    stack.append(ls[len(ls) - 1])
                    ls.pop()
                else:
                    possible = "No"
                    break

    print(possible)



