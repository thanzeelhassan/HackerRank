import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    dict = Counter(s)
    count = 0
    print(dict)
    list1 = list(dict.values())
    list2 = list1.copy()
    first_value = list1[0]
    print(first_value)
    result = True
    for i in list1 :
        if first_value != i :
            result = False
            break
    if result :
        return "YES"
    else :
        max_value = max(list1)
        print(max_value)
        index = list1.index(max_value)
        list1[index] = list1[index] - 1
        first_value = list1[0]
        print(list1)
        result = True
        for i in list1 :
            if first_value != i :
                result = False
                break
        if result :
            return "YES"
        else :
            min_value = min(list2)
            print(min_value)
            index = list2.index(min_value)
            list2[index] = list2[index] - 1
            if (list2[index] == 0):
                del list2[index]
            first_value = list2[0]
            print(list2)
            result = True
            for i in list2 :
                if first_value != i :
                    result = False
                    break
            if result :
                return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
