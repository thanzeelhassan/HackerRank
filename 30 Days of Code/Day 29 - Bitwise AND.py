import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    if K % 2 == 1:
        return K-1
    elif K | K-1 <= N:
        return K-1
    else:
        return K-2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')
    fptr.close()
