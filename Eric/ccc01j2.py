x = int(input())
m = int(input())



n = None

for i in range(m):
    if (x*i) % m == 1:
        n = i


if n == None:
    print('No such integer exists.')
else:
    print(n)