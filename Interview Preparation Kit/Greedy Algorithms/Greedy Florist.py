#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # k = number of friends
    # c = array
    # n = number of flowers
    n = len(c)
    # make an array to hold number of purchases
    purchases = [0] * k
    c.sort(reverse = True)
    result = 0
    while(n>0):
        fri = min(purchases)
        i = purchases.index(fri)
        flo = c[0]
        del c[0]
        result = result + flo * (fri+1)
        purchases[i] += 1
        n = n - 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
