import math
import os
import random
import re
import sys

def calc_cost(s,n):
    cost = 0
    for i in range(3):
        for j in range(3):
            temp = s[i][j] - n[i][j]
            if temp < 0:
                temp = temp *-1
            cost = cost + temp
    return cost

def formingMagicSquare(s):
    big_array = [[[6,7,2],[1,5,9],[8,3,4]],
                [[8,1,6],[3,5,7],[4,9,2]],
                [[4,3,8],[9,5,1],[2,7,6]],
                [[2,9,4],[7,5,3],[6,1,8]],
                [[8,3,4],[1,5,9],[6,7,2]],
                [[6,1,8],[7,5,3],[2,9,4]],
                [[2,7,6],[9,5,1],[4,3,8]],
                [[4,9,2],[3,5,7],[8,1,6]]]

    least_cost = calc_cost(s,big_array[0])

    for i in range(1,8):
        temp_cost = calc_cost(s,big_array[i])
        if temp_cost < least_cost :
            least_cost = temp_cost

    return least_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
