n = int(input())
name = []
value = []

for i in range(n):
    nm = input()
    name.append(nm)
    bids = input()
    value.append(bids)

highestbid = max(value)

for i in range(n):
    if value[i] == highestbid:
        print(name[i])