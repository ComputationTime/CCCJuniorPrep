def solve():
    n = int(input())
    k = int(input())
    l = gen_list(n, k, 1)
    print(l)


def gen_list(n, k, m):
    memo = []
    for i in range(n+1):
        l1 = []
        for j in range(k+1):
            l2 = []
            for z in range(n+1):
                l2.append(0)
            l1.append(l2)
        memo.append(l1)

    def gen(n, k, m):
        if memo[n][k][m] == 0:
            if k == 1 or n == k:
                memo[n][k][m] = 1
            else:
                c = 0
                for i in range(m, int(n/k)+1):
                    c += gen(n-i, k-1, i)
                memo[n][k][m] = c
        return memo[n][k][m]
    return gen(n, k, m)

solve()
