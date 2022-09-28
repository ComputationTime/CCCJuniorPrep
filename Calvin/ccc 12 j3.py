n = int(input)

def cool_print(n, *messages):
    for i in range(n):
        for message in messages:
            print(n*message, end = '')
        print()

cool_print(n, "*", 'x', "*")
cool_print(n, ' ', 'x', 'x')
cool_print(n, 'x', ' ', 'x')