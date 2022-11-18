a=str(input())


happy=0


for i in range (0,len(a)):
  if(a[i:i+3] ==":-)"):
    happy+=1

sad=0

for i in range (0,len(a)):
  if(a[i:i+3] ==":-("):
    sad+=1

if(happy==0 and sad==0):
  print("None")
elif(happy>sad):
  print("Happy")
elif(happy<sad):
  print("Sad")
else:
  print("Unsure")
