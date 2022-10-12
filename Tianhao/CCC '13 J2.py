word=input()
validWordList=["I", "O", "S", "H", "Z", "X", "N"]
isValid=True
for i in word:
  if i not in validWordList:
    isValid = False
    break
if isValid == True:
  print ("YES")
else:
  print ("NO")
