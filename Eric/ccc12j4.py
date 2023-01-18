alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

k = int(input())
word = input()

decoded = []

def decode(letter,p):
    shift = (3 * p) + k
    shift = shift % 26
    index = alphabet.index(letter)
    return alphabet[index-shift]


for i,letter in enumerate(word):
    decoded.append(decode(letter,i+1))

output = ''

for i in range(len(decoded)):
    output += decoded[i]

print(output)

    
    