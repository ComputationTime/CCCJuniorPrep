tine_height = int(input())
tine_spacing = int(input())
handle_length = int(input())

for _ in range(tine_height):
    line = '*' + ' ' * tine_spacing
    line *= 3
    line = line[0:-tine_spacing]
    print(line)

line = '*'*((tine_spacing)*2 + 3)

print(line)

for _ in range(handle_length):
    line = ' '*(1 + tine_spacing) + '*'
    print(line)