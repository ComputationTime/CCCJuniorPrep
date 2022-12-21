x = int(input())
y = int(input())
bx = int(input())
by = int(input())
steps = int(input())
counter = 1

crosstop = x-(bx*2)
crossside = y-(by*2)

grid = [[False for i in range(x)]for y in range(y)]


playerx = bx +1
playery = 1

print(grid)