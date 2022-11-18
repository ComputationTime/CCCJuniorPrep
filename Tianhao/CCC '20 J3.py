n = int(input())
listx = []
listy = []
for i in range(n):
  x,y = input().split(",")
  x = int(x)
  y = int(y)
  listx.append(x)
  listy.append(y)

print(str(min(listx) - 1) + "," + str(min(listy) - 1))
print(str(max(listx) + 1) + "," + str(max(listy) + 1))