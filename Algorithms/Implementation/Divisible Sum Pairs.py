import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#
from collections import Counter
def divisibleSumPairs(n, k, arr):
    result = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (arr[i] + arr[j]) % k == 0:
                result+=1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
