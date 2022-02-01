import math
import os
import random
import re
import sys
from collections import Counter
def whatFlavors(cost, money):
    dict = Counter(cost)
    if money % 2 == 0:
        half = int(money/2)
    else :
        half = money / 2
    if half in dict:
        if dict[half] >=2:
            print(cost.index(half)+1, end=" ")
            cost[cost.index(half)] = -1
            print(cost.index(half)+1)
            return
        else:
            dict.pop(half)
    for i in dict:
        if money-i in dict :
            print(cost.index(i)+1, end =" ")
            print(cost.index(money-i)+1)
            return

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
