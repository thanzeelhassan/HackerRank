#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    x = [0] * n
    x[0] = arr[0];
    x[1] = max(arr[1],x[0])
    for i in range(2,n):
        temp = arr[i] + x[i-2]
        x[i] = max(arr[i],temp,x[i-1])

    return x[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
