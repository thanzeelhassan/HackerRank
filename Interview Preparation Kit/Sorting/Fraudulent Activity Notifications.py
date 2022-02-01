#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def activityNotifications(expenditure, d):
    freq = {}
    notify=0
    def find(idx):
        total_count = 0
        for i in range(201):
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i
    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1
        #print(f"i: {i},val: {expenditure[i]}, freq: {freq}")
        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)
            #print("median: ",median)
            if expenditure[i+1]>= (median*2) :
                notify +=1
                #print("notify: ",notify)
            #remove the previous element from dictionary
            freq[expenditure[i-d+1]]-=1

    return notify

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
