import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def supersum(s):
    if len(s) == 1:
        return int(s)
    sum_ = 0
    for i in s:
        sum_ = sum_ + int(i)
    s = str(sum_)
    return supersum(s)
def superDigit(n, k):
    # Write your code here

    temp = supersum(str(n))
    temp = temp * k
    return supersum(str(temp))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
