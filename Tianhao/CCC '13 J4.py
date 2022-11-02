time = int(input())
numChores = int(input())
choreList = []
cnt = 0
for i in range(numChores):
  choreList.append(int(input()))

choreList.sort()

for i in choreList:
  if i <= time:
    time -= i
    cnt += 1

print(cnt)
