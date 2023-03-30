def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i

        else:
            stuart += len(string) - i

    if stuart == kevin:
        print("Draw")
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Stuart", stuart)


if __name__ == '__main__':
    s = input()
    minion_game(s)