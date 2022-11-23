phrase = input()
num_chars = len(phrase)

happy = 0
sad = 0

for index, letter in enumerate(phrase):
    if letter == ':':
        if index <= num_chars - 3:
            if phrase[index+1:index+3] == "-(":
                sad +=1
            elif phrase[index+1:index+3] == "-)":
                happy +=1

booleans = (happy>sad, sad>happy, happy==0)

match booleans:
    case (False, False, True):
        print('none')
    case (False, False, False):
        print('unsure')
    case (True, False, False):
        print('happy')
    case _:
        print('sad')