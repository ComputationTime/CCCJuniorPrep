n = int(input())
day1 = input()
day2 = input()
cnt = 0
for i in range(n):
    if day1[i] == day2[i] == 'C': cnt += 1
print(cnt)