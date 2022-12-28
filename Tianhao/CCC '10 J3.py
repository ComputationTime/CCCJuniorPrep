variables = {'A': 0, 'B': 0}

while True:
    text = input()
    values = text.split()
    ins = int(values[0])
    if ins == 1:
        variables[values[1]] = int(values[2])
    elif ins == 2:
        print(variables[values[1]])
    elif ins == 3:
        variables[values[1]] += variables[values[2]]
    elif ins == 4:
        variables[values[1]] *= variables[values[2]]
    elif ins == 5:
        variables[values[1]] -= variables[values[2]]
    elif ins == 6:
        variables[values[1]] //= variables[values[2]]
    else: 
        break