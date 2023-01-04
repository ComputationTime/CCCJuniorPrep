prev = int(input())
curr = int(input())

count = 2

while curr >= 0:
    count += 1
    placeholder = curr
    curr = prev - curr
    prev = placeholder
    

print(count-1)