import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    result = 0
    n = len(contests)
    imp = []
    non_imp = []
    for item in contests:
        if item[1] == 0:
            non_imp.append(item[0])
        else:
            imp.append(item[0])
    imp.sort()
    for item in non_imp:
        result+=item

    lose = []
    l = len(imp) - k
    for i in range(l):
        lose.append(imp[i])
        imp[i] = 0
    for item in imp:
        result+=item
    for item in lose:
        result-=item
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
