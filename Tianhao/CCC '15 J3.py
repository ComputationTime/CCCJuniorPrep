ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
VOWEL_INDEXES = [ALPHABETS.index("a"), ALPHABETS.index("e"), ALPHABETS.index("i"), ALPHABETS.index("o"), ALPHABETS.index("u")]

def follows(letter):
    consonants = "bcdfghjklmnpqrstwxyz"
    if letter == 'z':
        return 'z'
    return consonants[consonants.find(letter) + 1]

def closest_vowel(letter):
    alpha_index = ALPHABETS.index(char)
    differences = []

    for vowel in VOWEL_INDEXES:
        differences.append(abs(vowel - alpha_index))

    closest_vowel = VOWELS[differences.index(min(differences))]

    next_index = alpha_index + 1
    if next_index in VOWEL_INDEXES:
        next_index += 1

    return ALPHABETS[min(25, next_index)]

def solve():
    vowels = "aeiou"
    word = input()
    ret = ""
    for letter in word:
        if letter not in vowels:
            ret += letter
            ret += closest_vowel(letter)
            ret += follows(letter)
        else:
            ret += letter
    print(ret)

solve()