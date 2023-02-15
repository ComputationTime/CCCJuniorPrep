import itertools

N,K,M = input().split()
N = int(N)
K = int(K)
M = int(M)
bundles = 0
christmas = [int(i) for i in input().split()]
newyears = [int(i) for i in input().split()]


for i in range(N):
    for j in range(N):
        diff = i-j
        if diff < 0:
            diff*= -1
        if diff >= K and christmas[i] + newyears[j] == M:
            bundles += 1


print(bundles)