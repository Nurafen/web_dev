#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
#     ls = s.split()
#     st = ''
#     for el in ls:
#         st += el[0].upper() + el[1:] + ' '
    st = ''
    nums = [i for i in range(9)]
    for i in range(len(s)):
        if i == 0:
            st += s[i].upper()
        elif s[i - 1] == ' ' and s[i] != ' ' and s[i] not in nums:
            st += s[i].upper()
        else:
            st+= s[i]
    return st


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()