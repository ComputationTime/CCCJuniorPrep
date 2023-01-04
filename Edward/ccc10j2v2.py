a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())


def distance(s, forward, backward):
    position = 0 # distance from the starting line
    steps = 0 # number of steps taken regardless of positive or negative
    while steps < s:
        for _ in range(forward):
            position += 1
            steps += 1
            if steps == s:
                break
        if steps < s:
            for _ in range(backward):
                position -= 1
                steps += 1
                if steps == s:
                    break
    return position

nikki_distance = distance(s, a, b)
byron_distance = distance(s, c, d)
# Nikki vs Byron
if nikki_distance == byron_distance:
    print("Tied")
elif nikki_distance > byron_distance:
    print("Nikky")
elif nikki_distance < byron_distance:
    print("Byron")