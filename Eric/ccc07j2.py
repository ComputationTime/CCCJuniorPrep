dict = {
    'CU':'see you',
    ':-)':"I'm happy",
    ':-(':"I'm unhappy",
    ';-)':'wink',
    ':-P':'stick out my tongue',
    '(~.~)':'sleepy',
    'TA':'totally awesome',
    'CCC':'Canadian Computing Competition',
    'CUZ':'because',
    'TY':'thank-you',
    'YW':"you're welcome",
    'TTYL':'talk to you later'
}


while True:
    word = input()
    if word in dict:
        print(dict[word])
    else:
        print(word)
    if word == "TTYL":
        break
    