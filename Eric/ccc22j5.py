num = 5


def poolcheck(poolsize):
    count = 0 
    p = poolsize
    output = False
    for i in range(num -(p-1)):
        for j in range(i, i+p):
            for n in range(i, i+p):
                if yard[j][n]:
                    count += 1
        
        
    return output





yard = [[False for i in range(num)]for j in range(num)]




print(yard)

print(poolcheck(1))
