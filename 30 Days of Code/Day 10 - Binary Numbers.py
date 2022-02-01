import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    n = "{0:b}".format(int(n))
    longest = 0
    temp = 0
    for i in n:
        if i =='1':
            temp+=1
            continue
        if i == '0':
            if temp > longest:
                longest=temp
            temp =0
    if temp > longest:
        longest=temp
    print(longest)
