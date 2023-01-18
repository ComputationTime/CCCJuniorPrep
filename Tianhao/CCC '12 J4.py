number = int(input())
word = input()
for i in range(len(word)):
  shift = 3 * (i + 1) + number
  newp = ord(word[i]) - shift
  if newp < ord('A'):
    newp += 26
  print(chr(newp), end="")
