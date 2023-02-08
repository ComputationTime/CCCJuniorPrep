def closest_vowel(letter):
    vowels = "aeiou"
    m = 0 
    c = float('inf')
    for i, v in enumerate(vowels):
        value = abs(ord(letter) - ord(v))
        if value < c:
            c = value
            m = i
    return vowels[m]
        

def solve():
    x = input()
    consonants = "bcdfghjklmnpqrstvwxyz"
    ret = ""
    for c in x:
        if c in consonants:
            ret += c
            ret += closest_vowel(c)
            try:
                ret += consonants[consonants.index(c) + 1]
            except IndexError:
                ret += 'z'
        else:
            ret += c

    print(ret)


solve()