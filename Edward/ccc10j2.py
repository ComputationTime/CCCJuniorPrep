a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

steps = {"Nikky": 0, "Byron": 0}
c1, c2 = 0, 0


while c1 < s:
    print(steps)
    if steps["Nikky"] != 0 and steps["Nikky"] % a == 0 and c1 % a == 0:
        for _ in range(b):
            if c1 <= s:
                c1 += 1
                steps["Nikky"] -= 1
    else:
        c1 += 1
        steps["Nikky"] += 1

while c2 < s:
    print(steps)
    if steps["Byron"] != 0 and steps["Byron"] % c == 0 and c2 % c == 0:
        for _ in range(d):
            if c2 <= s:
                c2 += 1
                steps["Byron"] -= 1
    else:
        c2 += 1
        steps["Byron"] += 1

if steps["Nikky"] == steps["Byron"]:
    print("Tied")
else:
    print(max(steps, key=steps.get))