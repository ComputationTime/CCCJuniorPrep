num_of_cords = int(input())
min_x = 101
max_x = 1
min_y = 101
max_y = 1

for i in range(num_of_cords):
    xylist = input().split(',')
    if int(xylist[0]) < min_x:
        min_x = int(xylist[0])
    if int(xylist[0]) > max_x:
        max_x = int(xylist[0])
    if int(xylist[1]) < min_y:
        min_y = int(xylist[1])
    if int(xylist[1]) > max_y:
        max_y = int(xylist[1])

print(str(min_x-1)+','+str(min_y-1))
print(str(max_x+1)+','+str(max_y+1))
