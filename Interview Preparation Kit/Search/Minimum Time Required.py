#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    max_efficiency = min(machines)
    min_efficiency = max(machines)
    max_days = math.ceil(goal * min_efficiency / len(machines))
    min_days = math.ceil(goal * max_efficiency / len(machines))
    while min_days < max_days:
        temp = max_days - min_days
        middle = min_days + temp//2
        work = 0
        for i in machines:
            work += math.floor(middle / i)
        if work >= goal:
            max_days = middle
        else:
            min_days = middle+1

    return min_days
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    fptr.write(str(ans) + '\n')
    fptr.close()
