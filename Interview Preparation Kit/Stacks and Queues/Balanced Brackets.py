import math
import os
import random
import re
import sys

def isBalanced(s):
    stack = []
    dict1 = {")":"(","}":"{","]":"["}
    for i in s:
        if i in dict1.values():
            stack.append(i)
        elif len(stack) == 0:
            return "NO"
        elif stack[-1] != dict1[i]:
            return "NO"
        else:
            stack.pop()
    if len(stack)!= 0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
