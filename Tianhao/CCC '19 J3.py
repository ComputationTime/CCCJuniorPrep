n = int(input())
for i in range(n): 
  string = input() 
  cnt = 0 

  previousChar = string[0] 
  for character in string:
    if character == previousChar: 
      cnt += 1
    else: 
      print(cnt, end = " ")
      print(previousChar, end = " ")

      previousChar = character 
      cnt = 1 
  print(cnt, end = " ")
  print(previousChar, end = " ")
  print()