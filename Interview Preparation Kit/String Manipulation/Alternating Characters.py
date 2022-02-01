#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
from collections import Counter
def makeAnagram(a, b):
    # Write your code here
    dict1 = Counter(a)
    dict2 = Counter(b)
    dict3 = dict1 - dict2
    dict4 = dict2 - dict1
    count1 = 0
    count2 = 0
    for i in dict3:
        count1 = count1 + dict3[i]
    for i in dict4:
        count2 = count2 + dict4[i]
    return count1 + count2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
