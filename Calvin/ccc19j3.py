def printx(n, x):
    return str(n) + " " + x

m = int(input())
for i in range(m):
    sr = input()
    rs = ""
    x = sr[0]
    i = 1
    n = 1
    while i < len(sr):
        if sr[i] == x:
            n += 1
        else:
            rs += printx(n, x)+" "
            n = 1
            x = sr[i]
        i += 1
    rs += printx(n,x)
    print(rs)