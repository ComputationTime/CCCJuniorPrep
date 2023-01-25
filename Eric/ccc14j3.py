player1 = 100
player2 = 100

rounds = int(input())

for i in range(rounds):
    roll1,roll2 = input().split()
    if roll1 > roll2:
        player2 -= int(roll1)
    elif roll1 < roll2:
        player1 -= int(roll2)


print(player1)
print(player2)
