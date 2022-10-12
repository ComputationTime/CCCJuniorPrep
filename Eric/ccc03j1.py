t = int(input())
s = int(input())
h = int(input())

tine = ("*") + (" "*s) + ("*") + (" "*s) + ("*")

middle = ("*") + ("*"*s) + ("*") + ("*"*s) + ("*")

handle = (" ") + (" "*s) + ("*")
for _ in range(t):
    print(tine)

print(middle)

for _ in range(h):
    print(handle)