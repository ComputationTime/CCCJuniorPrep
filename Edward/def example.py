def follows(letter):
    consonants = "bcdfghjklmnpqrstwxyz"
    if letter == 'z':
        return 'z' 
    return consonants[consonants.find(letter) + 1]


def closest_vowel(letter):
    pass


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