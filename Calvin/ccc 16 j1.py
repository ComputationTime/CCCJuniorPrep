wins = 0

for i in range(6):
    x = input()
    if x == "W":
        wins = wins+1

if wins == 5 or 6:
    print('1')
elif wins == 3 or 4:
    print("2")
elif wins == 1 or 2:
    print("3")
else:
    print("-1")