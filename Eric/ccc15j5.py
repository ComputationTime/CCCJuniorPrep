n = int(input())
k = int(input())


import math

count = 0
def solve(n,k,t):
    global count

    if n == k or k == 1:
        # print(n,k,t)
        count +=1
        return 1
    if n < k:
        return 0

    
    for i in range(t,math.floor(n/k)+1):
        solve(n-i,k-1,i)

'7,3,1 6,3,2 6,2,1 5,1,2'

    
solve(n,k,1)
print(count)

