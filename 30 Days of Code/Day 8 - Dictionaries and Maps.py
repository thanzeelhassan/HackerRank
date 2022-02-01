n = int(input())
dict1 = {}
for i in range(n):
    name,no = input().split()
    dict1[name] = no

while True:
    try:
        temp = input()
        if temp in dict1 :
            print('%s=%s' % (temp, dict1[temp]))
        else:
            print("Not found")
    except:
        break
