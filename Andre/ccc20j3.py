num_points = int(input())

x = []
y = []

for _ in range(num_points):
    xp, yp = tuple(map(int, input().split(sep=", ")))
    x.append(xp)
    y.append(yp)

bottom_left = (min(x)-1, min(y)-1)
top_right = (max(x)+1, max(y)+1)

print(f"{bottom_left[0]}, {bottom_left[1]}\n{top_right[0]}, {top_right[1]}" )