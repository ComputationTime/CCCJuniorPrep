line = list(input())

happy = 0
sad = 0 
while len(line) > 0:
    eye = line.pop(0)
    if eye == ':':
        nose = line.pop(0)
        if nose == '-':
            mouth = line.pop(0)
            if mouth == ')':
                happy += 1
            elif mouth == '(':
                sad += 1


if happy == 0 and sad == 0:
    print('none')

elif happy > sad:
    print('happy')

elif happy < sad:
    print('sad')

else: 
    print('unsure')

    
