num_lines = int(input())
output = ''
for _ in range(num_lines):
    line = list(input())
    line.append(0)
    # print(line)
    # +++===!!!!
    i = 0
    while i < len(line):
        current = line[i]
        if current == 0:
            break
        for j, subsequent in enumerate(line[i+1:]): # +++===!!!!
            if subsequent != current:
                break
        num_repeated = j+1
        i += num_repeated
        output += f'{num_repeated} {current} '
    output += '\n'

print(output)


- - 3 + 2 1 9
 3  2 1 + - 9 -




