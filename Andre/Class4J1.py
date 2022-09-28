H = int(input())

# for loop that prints going up

for i in range(H//2+1):
    # print * left
    for j in range(1 + 2*i):
        print('*', end='')
    # print spaces
    for j in range(2*H - 4 * i - 2):
        print(' ', end='')
    # print * right 
    for j in range(1 + 2*i):
        print('*', end='')
    print()

# for loop that goes down

#

for i in range(H//2):
    # print * left
    k = H//2 - i - 1
    for j in range(1 + 2*k):
        print('*', end='')
    # print spaces
    for j in range(2*H - 4 * k - 2):
        print(' ', end='')
    # print * right 
    for j in range(1 + 2*k):
        print('*', end='')
    print()