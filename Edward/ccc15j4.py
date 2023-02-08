def solve():
    m = {}
    c = {}
    check = []
    n = int(input())
    j = 0
    for _ in range(n):
        letter, val = input().split()
        val = int(val)
        if letter == "R":
            m[val] = j
            check.append(val)
        if letter == "S":
            if val not in c:
                c[val] = j - m[val]
            else:
                c[val] += j - m[val]
            try:
                check.remove(val)
            except ValueError:
                c[val] = -1
        if letter == "W":
            j += (val - 1)
        else:
            j += 1
    for val in check:
        c[val] = -1
    for k, v in sorted(c.items()):
        print(k, v)


solve()