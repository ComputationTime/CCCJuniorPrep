n = int(input())
line1 = input()
line2 = input()

count = 0

for i in range(n):
    lot1 = line1[i]
    lot2 = line2[i]
    if lot1 == 'C' and lot2 == 'C':
        count +=1

print(count)
