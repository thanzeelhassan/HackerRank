import math
import os
import random
import re
import sys

def getWays(n, c):
    dp = [1] + [0]*n
    for coin in c:
        for i in range(coin,n+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, c)
    fptr.write(str(ways) + '\n')
    fptr.close()
