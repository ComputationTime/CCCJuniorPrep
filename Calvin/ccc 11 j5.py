def goodNumber(N, x):
    last = N
    ok = True
    while x > 0 and ok:
        digit = x % 10
        ok = digit < last
        last = digit
        x = x // 10
    return ok

def goodCombo(N,x,l):


    digits = []
    while x > 0:
        digits.append(x % 10)
        x = x // 10

    for d in digits:
        for x in range(0,N-1):
            if d == l[x]:
                if (x+1) not in digits:
                    return False
    return True