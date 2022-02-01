import math
import os
import random
import re
import sys
from collections import Counter

def sherlockAndAnagrams(s):
    count = 0
    dic = Counter(s) # all 1 length substrings
    for i in range(2,len(s)):
        sb = s[0:i]
        l=len(sb)
        sb = sorted(sb) # sort in order
        sb="".join(sb) # convert to string
        dic[sb]+=1 # add to dictionary
        for j in range(1,len(s)):
            if j + l <= len(s):
                sb = s[j:j+l] # slice
                sb = sorted(sb) # sort in order
                sb="".join(sb) # convert to string
                dic[sb]+=1 # add to dictionary
    for k,v in dic.items():
        count += v * (v-1) // 2

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
