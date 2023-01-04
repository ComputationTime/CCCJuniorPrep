a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

steps = 0 + s

Nikky = 0
Byron = 0

while steps != 0:
    if a > steps:
        Nikky += steps
        steps -= steps
    else:
        Nikky += a
        steps -= a
    if b > steps:
        Nikky -= steps
        steps -= steps
    else:
        Nikky -= b
        steps -= b

steps = 0 + s

while steps != 0:
    if c > steps:
        Byron += steps
        steps -= steps
    else:
        Byron += c
        steps -= c
    if d > steps:
        Byron -= steps
        steps -= steps
    else:
        Byron -= d
        steps -= d



if Nikky > Byron:
    print('Nikky')
elif Nikky < Byron:
    print('Byron')
else: 
    print('Tied')
