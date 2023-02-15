q = int(input())
n = int(input())
d = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
output = 0

if q == 2:
    d = sorted(d)
    p = sorted(p)[::-1]
    for i in range(n):
        p1 = d[i]
        p2 = p[i]
        output += max(p1,p2)
if q == 1:
    d = sorted(d)
    p = sorted(p)
    for i in range(n):
        p1 = d[i]
        p2 = p[i]
        print(p1,p2)
        output += max(p1,p2)
        


print(output)