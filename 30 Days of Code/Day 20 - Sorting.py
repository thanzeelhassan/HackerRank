import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    totalswaps = 0
    for i in range(0,n):
        numberOfSwaps = 0
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numberOfSwaps+=1
        totalswaps +=numberOfSwaps
        if numberOfSwaps == 0:
            break
    print("Array is sorted in", totalswaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
