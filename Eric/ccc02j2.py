quit = False

while quit != True:
    word = input()
    if word =='quit!':
        quit = True
    elif len(word) <= 4:
        print(word)
    else:
        if word[-3] not in "aeiouy":
            print(word.replace('or','our'))
        else:
            print(word)

  
    
            

