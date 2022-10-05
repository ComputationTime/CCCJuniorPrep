x = int(input())
message = []

for i in range(x):
    message.append(input().split())

for i in message:
    print(i[1] * int(i[0]))