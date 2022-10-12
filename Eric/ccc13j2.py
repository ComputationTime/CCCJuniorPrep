
word = input()

allowed_letters = ["I", "O", "S", "H", "Z", "X", "N"]


Answer = True

for i in word:
    if i not in allowed_letters:
        Answer = False

if Answer:
    print("YES")
else:
    print("NO")

