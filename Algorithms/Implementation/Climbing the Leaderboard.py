import math
import os
import random
import re
import sys

from collections import Counter
import bisect
def climbingLeaderboard(ranked, player):
    result = []
    list_set = set(ranked)
    list_ = (list(list_set))
    list_.sort()
    n = len(list_)
    for item in player:
        temp = bisect.bisect_right(list_,item)
        result.append(n-temp+1)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
