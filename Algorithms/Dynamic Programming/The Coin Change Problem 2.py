import math
import os
import random
import re
import sys

def getWays(n, c, memo):
    if n == 0:
        return 1
    if len(c) == 0:
        return 0
    if n < 0:
        return 0
    s = ""
    for item in c :
        s = s + str(item)
    temp = str(n) + ":" +s
    if temp in memo:
        return memo[temp]
    first = getWays(n-c[0],c,memo)
    second = getWays(n,c[1:],memo)
    memo[temp] = first + second
    return first + second

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    memo = {}
    ways = getWays(n, c,memo)
    fptr.write(str(ways) + '\n')
    fptr.close()
