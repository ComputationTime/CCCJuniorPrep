N = int(input())
T = int(input())
maxpool = 0


def poolcheck(x,y,poolsize):
    global yard
    global N
    qualify = True
    if (x + poolsize) > N or (y + poolsize) > N:
        return poolsize - 1
    for i in range(poolsize):
        if yard[y+i-1][x+poolsize-1] == 1:
            qualify = False
            break
        if 1 in yard[y+i][x:x+poolsize]:
            qualify = False
            break
        
    if qualify:
        return poolcheck(x,y,poolsize+1)
    else:
        return poolsize - 1

    
        

yard = [[0 for i in range(N)]for j in range(N)]


for i in range(T):
    x,y = input().split()
    x = int(x)
    y = int(y)
    yard[x-1][y-1] = 1

for i in range(N):
    for j in range(N):
        if yard[i][j] == 1:
            continue
        else:
            size = poolcheck(i,j,2)
            if size > maxpool:
                maxpool = size
print(maxpool)





