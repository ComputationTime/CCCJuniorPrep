def solve():
    antonia, david = 100, 100
    n = int(input())


    for i in range(1, n+1):
        roll1, roll2 = [int(x) for x in input().split()]
        if roll1 == roll2:
            continue
        if roll1 > roll2:
            david -= roll1
        if roll2 > roll1:
            antonia -= roll2

    print(antonia)
    print(david)

solve()