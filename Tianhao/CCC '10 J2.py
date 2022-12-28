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

print(nikky_steps)