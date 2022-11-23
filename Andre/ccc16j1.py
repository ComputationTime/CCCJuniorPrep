matches = []
for _ in range(6):
    matches.append(input())

f = lambda letter : letter == 'W'


win_boolean_array = list(map(f, matches))
num_wins = sum(win_boolean_array)


# could have been easier to implement with if statements
group = 3 - (num_wins - 1) // 2

if group == 4:
    print(-1)
else:
    print(group)