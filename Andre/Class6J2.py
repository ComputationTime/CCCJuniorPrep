letters = {'I', 'O', 'S', 'H', 'Z', 'X', 'N'}
word = input()
valid = not False in map(lambda letter:letter in letters, word)
if valid:
    print('YES')
else:
     print('NO')
