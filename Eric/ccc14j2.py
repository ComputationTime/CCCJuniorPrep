votes = int(input())
AB_votes = input()

A_votes = 0
B_votes = 0

for i in range(votes):
    if AB_votes[i] == "A":
        A_votes += 1
    elif AB_votes[i] == "B":
        B_votes += 1

if A_votes > B_votes:
    print("A")
elif A_votes < B_votes:
    print("B")
else:
    print("Tie")
