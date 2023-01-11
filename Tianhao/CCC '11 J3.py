t1 = int(input())
t2 = int(input())

tmp = t2
cnt = 0

while tmp >= 0:
    tmp = t1-t2
    t1=t2
    t2=tmp
    cnt+=1

print(cnt+1)