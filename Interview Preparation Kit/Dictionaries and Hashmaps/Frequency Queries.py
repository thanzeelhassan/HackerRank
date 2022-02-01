import math
import os
import random
import re
import sys
from collections import Counter
def freqQuery(queries):
    n = len(queries)
    dict = {}
    dict_frequencies = {}
    result = []
    for i in range(n):
        if queries[i][0] == 1:
            x = queries[i][1]
            if x in dict:
                if dict_frequencies[dict[x]]:
                    dict_frequencies[dict[x]] = dict_frequencies.get(dict[x],0) - 1
                    if dict_frequencies[dict[x]] == 0:
                        dict_frequencies.pop(dict[x])
            dict[x] = dict.get(x,0) + 1
            dict_frequencies[dict[x]] = dict_frequencies.get(dict[x],0) + 1
        elif queries[i][0] == 2:
            y = queries[i][1]
            if y in dict:
                if dict[y] == 1:
                    dict.pop(y)
                    dict_frequencies[1] = dict_frequencies[1] - 1
                    if dict_frequencies[1] == 0:
                        dict_frequencies.pop(1)
                else:
                    dict_frequencies[dict[y]] = dict_frequencies.get(dict[y],0) - 1
                    dict[y] = dict[y] - 1
                    dict_frequencies[dict[y]] = dict_frequencies.get(dict[y],0) + 1
        elif queries[i][0] == 3:
            z = queries[i][1]
            if z in dict_frequencies :
                if dict_frequencies[z] >0:
                    result.append(1)
                else:
                    result.append(0)
            else:
                result.append(0)

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
