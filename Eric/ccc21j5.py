m = int(input())
n = int(input())
k = int(input())
output = 0
painting = [['B' for i in range(n)]for i in range(m)]
duplicates = []
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
    paint(rc,int(num))


for row in painting:
    for tile in row:
        if tile == 'G':
            output+= 1



print(output)





