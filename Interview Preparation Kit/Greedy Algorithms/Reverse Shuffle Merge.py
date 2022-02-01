import math
import os
import random
import re
import sys
# Complete the 'reverseShuffleMerge' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
from collections import Counter
def reverseShuffleMerge(s):
    dict1 = Counter(s)
    #print(s)
    #print(dict1)
    dict2 = {}
    for i in dict1:
        dict2[i] = int(dict1[i] / 2)

    #print(dict2)
    s = "".join(reversed(s))
    #print(s)
    list1 = []
    n = 0
    for i in dict2:
        n = n + dict2[i]
    for i in range(0,len(s)-n +1):
        j = i + n
        list1.append(s[i:j])
    #print(list1)
    result = list1[0]
    for item in list1:
        temp = Counter(item)
        #print(temp)
        if temp == dict2:
            #print("YES")
            if item < result:
                #print("Changed")
                result = item
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
