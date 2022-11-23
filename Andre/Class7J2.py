num_votes = int(input())

votes = input()

A = 0
B = 0

for letter in votes:
    if letter =='A':
        A += 1
    elif letter == 'B':
        B += 1
if A == B:
    print('Tie')
elif A>B:
    print('A')
else:
    print('B')