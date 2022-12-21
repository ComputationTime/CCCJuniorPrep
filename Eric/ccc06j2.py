dice1 = int(input())
dice2 = int(input())

solutions = []

count = 0

for i in range(1,dice1+1):
    for j in range(1,dice2+1):
        if i + j == 10:
            count +=1
            solutions.append((i,j))
if count == 1:
    print(f'There is {count} way to get the sum 10.')
else:
    print(f'There are {count} ways to get the sum 10.')
