# import matplotlib.pyplot as plt
level,width,x = input().split()
level = int(level)
width = int(width)
x = int(x)


# x_list = []
# y_list = []

point_list = [(0,1),(width,1)]


def level_up(Ax,Ay,Bx,By):
    x_change = Bx - Ax
    y_change = By - Ay
    if x_change != 0:
        l = x_change // 3
        point_list.append((Ax,Ay))
        point_list.append((Ax + l,Ay))
        point_list.append((Ax + l,Ay + l))
        point_list.append((Ax + (l * 2),Ay + l))
        point_list.append((Ax + (l * 2),Ay))
        point_list.append((Ax + (l * 3),Ay))
    else:
        l = y_change // 3
        point_list.append((Ax,Ay))
        point_list.append((Ax,Ay+l))
        point_list.append((Ax - l,Ay + l))
        point_list.append((Ax - l,Ay + (l * 2)))
        point_list.append((Ax,Ay  + (l * 2)))
        point_list.append((Ax,Ay  + (l * 3)))


for i in range(level):
    point_count = len(point_list)
    for i in range(len(point_list)-1):
        point1 = point_list[i]
        Ax = point1[0]
        Ay = point1[1]
        point2 = point_list[i+1]
        Bx = point2[0]
        By = point2[1]
        level_up(Ax,Ay,Bx,By)
    for _ in range(point_count):
        point_list.pop(0)

# for i in point_list:
#     x_list.append(i[0])
#     y_list.append(i[1])

    

output_list = []



for i in range(0,len(point_list)-1):
    point1 = point_list[i]
    point2 = point_list[i+1]
    if x in range(point1[0],point2[0]) or x in range(point2[0],point1[0]):
        output_list.append(point1[1])

for point in point_list:
    if point[0] == x and point[1] not in output_list:
        output_list.append(point[1])

output_list = sorted(output_list)

output = ' '.join(map(str,output_list))

print(output)

# plt.plot(x_list, y_list, '-o')
# plt.show()
       

