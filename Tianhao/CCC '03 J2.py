import math
n = int(input())
while n != 0:
    for i in range(math.floor(math.sqrt(n)),0,-1):
        if n % i == 0:
            j = n // i
            print("Minimum perimeter is",2*(i+j),"with dimensions",i,"x",j)
            break
    n = int(input())