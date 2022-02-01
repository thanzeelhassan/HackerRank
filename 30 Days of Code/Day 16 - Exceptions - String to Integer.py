import math
import os
import random
import re
import sys

S = input()
try:
    temp = int(S)
    print(temp)
except ValueError:
    print("Bad String")