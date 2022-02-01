import math
import os
import random
import re
import sys
from collections import Counter
def pairs(k, arr):
    dict1 = Counter(arr)
    result = 0
    for i in dict1:
        if i+k in dict1:
            result = result +1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
