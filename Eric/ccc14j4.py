k = int(input())
r = int(input())
friendlist = []

for i in range(1,k+1):
    friendlist.append(i)


for _ in range(r):
    removelist = []
    n = int(input())
    count = 0
    for i in range(len(friendlist)):
        count += 1
        if count == n:
            removelist.append(friendlist[i])
            count = 0
    for i in removelist:
        friendlist.remove(i)

friendlist = sorted(friendlist)
for i in friendlist:
    print(i)


