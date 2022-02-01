#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    n = len(q)
    for i in range(n):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
    sum = 0
    for i in range(n):
        for j in range(max(q[i]-2,0),i):
            if(q[j] > q[i]):
                sum = sum + 1

    print(sum)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
