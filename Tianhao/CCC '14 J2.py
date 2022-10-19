length=int(input())
votes=input()

aCount = votes.count('A')
bCount = votes.count('B')

if aCount < bCount:
    print("B")
elif aCount == bCount:
    print("Tie")
else:
    print("A")
