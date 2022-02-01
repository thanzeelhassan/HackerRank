import math
import os
import random
import re
import sys

def birthday(arr, s, l):
    current_sum = 0
    count = 0
    for i in range(0,l):
        current_sum +=arr[i]

    if current_sum == s :
        count+=1

    for i in range(l,len(arr)):
        current_sum = current_sum + arr[i]
        current_sum = current_sum - arr[i-l]
        if current_sum == s:
            count+=1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
