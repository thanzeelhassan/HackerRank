import math
import os
import random
import re
import sys
from math import sqrt

def factors(N):
    if N == 1:
        return [1]
    temp1=sqrt(N)
    temp2=int(temp1)
    factors=[1,N]
    if(temp1==temp2):
        for i in range (2,temp2):
            if(N%i==0):
                factors.append(i)
                factors.append(N//i)
        factors.append(temp2)
    else:
        for i in range (2,temp2+1):
            if(N%i==0):
                factors.append(i)
                factors.append(N//i)
    return factors

def getTotalX(a, b):
    total_count = 0
    # find all factors of b
    arr = factors(b[0])
    for i in range(1,len(b)):
        temp = factors(b[i])
        temp_array = []
        for item in temp :
            if item in arr  :
                temp_array.append(item)
        arr = temp_array
    for i in range(len(arr)):
        count = 0
        for j in range(len(a)):
            if arr[i] % a[j] == 0:
                continue
            else :
                count +=1
        if count == 0:
            total_count +=1
    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()
