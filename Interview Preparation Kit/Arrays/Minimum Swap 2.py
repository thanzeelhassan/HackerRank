#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    value = 0
    i=1
    while(i<=len(arr)):
        if arr[i-1] != i:
            temp = arr[i-1]
            arr[i-1] = arr[temp-1]
            arr[temp-1] = temp
            value = value+1
        else :
            i = i +1
    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
