quit = False

while quit != True:
    word = input()
    if word =='quit!':
        quit = True
    elif len(word) <= 4:
        pass
    else:
        if word[-3] not in "aeiouy" and word[-2:] == "or":
            print(word.replace(word[-2:],'our'))
        else:
            print(word)

  
    
            

