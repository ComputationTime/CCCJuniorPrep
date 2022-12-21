time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 
'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 
'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2, 
'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 
't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 
'y': 3, 'z': 4}

keys = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']



count = 0
while True:
    line = input()
    if line == 'halt':
        break
    else:
        prevkey = 1
        for letter in line:
            count += time[letter]
            if prevkey == 1:
                for i in range(8):
                    if letter in keys[i]:
                        prevkey = i
            else:
                for i in range(8):
                    if letter in keys[i]:
                        currkey = i
                if currkey == prevkey:
                    count +=2
                prevkey = currkey
            
        print(count)
    count = 0 


