n = int(input())
values = []

for x in range(n):
    y = n-x
    if x <= 5 and y <= 5:
        if [y, x] not in values and [x, y] not in values:
            values.append([y, x])


print(values)