#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mergeSort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        count = count + mergeSort(L)
        count = count + mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i]<=R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                count = count + 1
                j+=1

            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    return count
def countInversions(arr):
    # Write your code here
    n = len(arr)
    count = mergeSort(arr)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
