#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
dict1 = {}
def stepPerms(n):
    # Write your code here
    #find for n = n-1,n-2,n-3
    if n in dict1:
        return dict1[n]
    if n <= 0:
        dict1[n] = 0
        return 0
    if n == 1:
        dict1[n] = 1
        return 1
    if n == 2:
        dict1[n] = 2
        return 2
    if n == 3:
        dict1[n] = 4
        return 4
    temp = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    dict1[n] = temp
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
