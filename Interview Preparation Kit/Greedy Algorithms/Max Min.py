#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    n = len(arr)
    arr2 = [0] * k
    min_result = float("INF")
    arr.sort()
    arr2 = arr[0:k]
    result = arr2[k-1] - arr2[0]
    if result < min_result:
        min_result = result
    for i in range(k,n):
        del arr2[0]
        arr2.append(arr[i])
        result = arr2[k-1] - arr2[0]
        if result < min_result:
            min_result = result

    return min_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
