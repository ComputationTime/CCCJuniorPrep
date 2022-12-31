'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky = 0
byron = 0

nikky_steps = [1] * a + [0] * b
l1 = len(nikky_steps)

byron_steps = [1] * c + [0] * d
l2 = len(byron_steps)

for i in range(s):
    nikky += nikky_steps[i % l1]
    byron += byron_steps[i % l2]

if nikky > byron:
    print('Nikky')
elif nikky < byron:
    print('Byron')
else:
    print('Tied')
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

def distance(s, forward, backward):
    position = 0
    steps = 0
    while steps < s:
        for x in range(forward):
            position += 1
            steps += 1
            if steps == s:
                break
        if steps < s:
            for x in range(backward):
                position -= 1
                steps += 1
                if steps == s:
                    break
    return position

nikki_distance = distance(s, a, b)
byron_distance = distance(s, c, d)

if nikki_distance == byron_distance:
    print("Tied")
elif nikki_distance > byron_distance:
    print("Nikki")
elif nikki_distance < byron_distance:
    print("Byron")