icon=['*', 'x', '*'], [' ', 'x', 'x'], ['*', ' ', '*']
k = int(input())
for r in icon:
    for i in range(k):
        for p in r:
            print(k * p, end='')
        print()