m = int(input())
n = int(input())
k = int(input())
output = 0
painting = [['B' for i in range(n)]for i in range(m)]
duplicates = []
paintlist = []
def paint(rc,num):
    num -= 1
    if rc == 'R':
        for i in range(n):
            if painting[num][i] == 'B':
                painting[num][i] = 'G'
            else:
                painting[num][i] = 'B'
    else:
        for i in range(m):
            if painting[i][num] == 'B':
                painting[i][num] = 'G'
            else:
                painting[i][num] = 'B'




for i in range(k):
    rc,num = input().split()
    if (rc,num) in duplicates:
        duplicates.remove((rc,num))
    else:
        paintlist.append((rc,num))
for i in paintlist:
    paint(i[0],int(i[1]))


for row in painting:
    for tile in row:
        if tile == 'G':
            output+= 1



print(output)





