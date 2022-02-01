
import math
import os
import random
import re
import sys

def solve(n):
    # Write your code here
    if n == 1:
        return -1
    if n == 2 :
        return -1
    if n % 4 == 0:
        return 3
    if n % 4 == 1:
        return 2
    if n % 4 == 2 :
        return 4
    if n % 4 == 3 :
        return 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = solve(n)
        fptr.write(str(result) + '\n')
    fptr.close()
