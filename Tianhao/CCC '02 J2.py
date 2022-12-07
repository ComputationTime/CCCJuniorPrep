vowelList = ["a", "e", "i", "o", "u", "y"] 

while True: 
  word = input()
  if word == "quit!":
      break

  if word.endswith("or") and len(word) > 4 and word[-3] not in vowelList: 
    word = word[0: len(word)-2] + "our"

  print(word)
