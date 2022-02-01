import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    list1 = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        if emailID[-10:] == "@gmail.com":
            list1.append(firstName)
    list1.sort()
    for item in list1:
        print(item)
