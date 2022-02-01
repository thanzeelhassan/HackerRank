# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def checkprime(n):
    if n == 1:
        print("Not prime")
        return
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")
t = int(input())
for i in range(t):
    n = int(input())
    checkprime(n)
