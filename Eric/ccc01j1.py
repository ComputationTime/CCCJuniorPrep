H = int(input())
linelist = []
gap = 0
increase = 1

for i in range(H//2):
    gap = H * 2 - increase - increase
    print((increase * "*") + (gap*" ") + (increase * "*"))
    increase += 2



increase-=2

print(int(H * 2) * "*")

for i in range(H//2):
    gap = H * 2 - increase - increase
    print((increase * "*") + (gap*" ") + (increase * "*"))
    increase -= 2











