h = int(input())
m = int(input())

possible = False

for i in range(1,m+1):
    t = i
    A = -6*(t*t*t*t) + h*(t*t*t) + 2*(t*t) + t
    if A <= 0:
        output = i
        possible = True
        break

if possible:
    print('The balloon first touches ground at hour:')
    print(output)
else:
    print('The balloon does not touch ground in the given time.')