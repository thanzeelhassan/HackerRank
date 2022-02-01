#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    result = 0
    for i in range(0,len(b)):
        temp1 = 0
        for j in range(0,len(a)):
            if a[j] <= b[i]:
                temp1 +=1
        temp2 = 0
        for j in range(0,len(c)):
            if c[j]<=b[i]:
                temp2+=1
        result += temp1*temp2
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
