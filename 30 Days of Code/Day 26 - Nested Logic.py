'''
rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
'''
t = input()
d1 , m1, y1 = t.split(" ")
t = input()
d2 , m2, y2 = t.split(" ")
fine = 0
d1 = int(d1)
m1 = int(m1)
y1 = int(y1)

d2 = int(d2)
m2 = int(m2)
y2 = int(y2)

if y1 < y2:
    fine = 0
elif y1 == y2 and m1 < m2:
    fine = 0
elif y1 ==y2 and m1 == m2 and d1 < d2 :
    fine = 0

if y1 > y2 :
    fine = 10000
elif y1 == y2 and m1 > m2 :
    fine = 500 * (m1-m2)
elif y1 == y2 and m1 == m2 and d1 > d2 :
    fine = 15 * (d1-d2)

print(fine)
