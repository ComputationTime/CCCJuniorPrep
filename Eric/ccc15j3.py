dict = {'bc':'a','dfg':'e','hjkl':'i','mnpqr':'o','stvwxyz':'u'}
alphabet = list('abcdefghijklmnopqrstuvwxyz')
vowels = 'aeiou'
word = list(input())
output = ''



for l in word:
    if l in vowels:
        output += l
    else:   
        output += l
        for i in dict:
            if l in i:
                output += dict[i]
        if l == 'z':
            output += l
        else:
            for i in range(len(alphabet)):
                if l == alphabet[i]:
                    if alphabet[i+1] in vowels:
                        output += alphabet[i+2]
                    else:
                        output += alphabet[i+1]
                    break

print(output)
