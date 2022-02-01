import math
import os
import random
import re
import sys
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    maxsum = 0
    for i in range(1,5):
        for j in range(1,5):
            tempsum = 0
            tempsum = tempsum + arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            tempsum = tempsum + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            if(i==1 and j==1):
                maxsum = tempsum
                continue
            if tempsum > maxsum:
                maxsum = tempsum
    print(maxsum)
