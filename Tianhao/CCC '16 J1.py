w=0
for i in range(6):
    if input()=='W':
        w+=1
        
if w > 4: print(1)
elif 2 < w < 5: print(2)
elif 0 < w < 3: print(3)
else: print(-1)
