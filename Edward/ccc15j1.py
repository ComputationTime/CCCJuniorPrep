x1 = int(input())
x2 = int(input())

if x1 == 2 and x2 == 18:
    print("Special")
elif x1 == 2 and x2 < 18:
    print("Before")
elif x1 == 2 and x2 > 18:
    print("After")
elif x1 < 2: 
    print("Before")
else:
    print("After")