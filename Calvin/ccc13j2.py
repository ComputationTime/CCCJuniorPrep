string = input()
fail = False

for i in range(len(string)):
  if string[i] == 'I' or string[i] == 'O' or string[i] == 'S' or string[i] == 'H':
    fail = False
  elif string [i] == 'Z' or string[i] == 'X' or string[i] == 'N':
    fail = False
  else:
    print ("NO")
    fail = True
    break
    
if fail == False:
  print ("YES")