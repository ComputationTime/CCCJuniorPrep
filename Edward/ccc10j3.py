A, B = 0, 0
def parse(arg1):
    if arg1 == 'A':
        return int(A)
    else:
        return int(B)
while True:
    line = input()
    arguments = line.split()
    num = int(arguments[0])
    if num == 1:
        if arguments[1] == 'A':
            A = arguments[2]
        else:
            B = arguments[2]
    if num == 2:
        if arguments[1] == 'A':
            print(A)
        else:
            print(B)
    if num == 3:
        val = parse(arguments[1]) + parse(arguments[2])
        if arguments[1] == 'A':
            A = val
        else:
            B = val
    if num == 4:
        val = parse(arguments[1]) * parse(arguments[2])
        if arguments[1] == 'A':
            A = val
        else:
            B = val
    if num == 5:
        val = parse(arguments[1]) - parse(arguments[2])
        if arguments[1] == 'A':
            A = val
        else:
            B = val
    if num == 6:
        val = parse(arguments[1]) / parse(arguments[2])
        val = int(val)
        if arguments[1] == 'A':
            A = val
        else:
            B = val
    if num == 7:
        break
    
    