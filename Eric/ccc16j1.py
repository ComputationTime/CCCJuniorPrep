wins = 0

for i in range(6):
    game = input()
    if game == "W":
        wins += 1

if wins == 0:
    print("-1")

elif wins == 1 or wins == 2:
    print("3")

elif wins == 3 or wins == 4:
    print("2")

else:
    print("1")
