import math
import os
import random
import re
import sys

def DFSrec(adj,s,visited,val):
    visited[s] = 1
    val += 1
    for i in adj[s]:
        if visited[i]==0:
            val = DFSrec(adj,i,visited,val)
    return val

def make_adjacency_matrix(cities,n):
    adj = dict()
    for i in cities:
        #print("i",i)
        if i[0] in adj:
            adj[i[0]].append(i[1])
        else:
            adj[i[0]] = [i[1]]
        if i[1] in adj:
            adj[i[1]].append(i[0])
        else:
            adj[i[1]] = [i[0]]
    for i in range(1,n+1):
        if i in adj:
            pass
        else:
            adj[i] = []
    return adj

def find_loops_components(n,adj):
    visited = [0]*(n+1)
    countNodes = 0
    countComponents = 0
    l = []
    for i in range(1,n+1):
        if visited[i]==0:
            val = 0
            nodes = DFSrec(adj,i,visited,val)
            countComponents += 1
            l.append(nodes)
    return l,countComponents

def roadsAndLibraries(n, c_lib, c_road, cities):
    # print("n",n)
    # print("c_lib",c_lib)
    # print("c_road",c_road)
    # print("cities",cities)
    if c_road>c_lib:
        return n*c_lib
    else:
        ##adjacency matrix construction
        adj = make_adjacency_matrix(cities,n)
        #print("adj",adj)
        ##algorithm
        l,countComponents = find_loops_components(n,adj)
        #print("l",l)
        #print("countComponents",countComponents)
        total = 0
        for i in l:
            total = total + (c_road*(i-1))
        total = total + countComponents*c_lib
        return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')
    fptr.close()
