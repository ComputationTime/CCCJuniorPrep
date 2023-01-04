n = int(input())
ways = 0
used_numbers = []
for i in range(1,6):
    for j in range(1,6):
        if i + j == n:
            if i not in used_numbers and j not in used_numbers:
                used_numbers.append(i)
                used_numbers.append(j)
                ways += 1

if n < 6:
    ways +=1

print(ways)
