def solve():
    happy = ":-)"
    sad = ":-("
    x = input()
    h, s = 0, 0
    l, r = 0, 3 
    if len(x) <= 2:
        print("none")
        return 

    while l < r and r < len(x)+1:
        word = x[l:r]
        if word == happy:
            h += 1
        if word == sad:
            s += 1
        l, r = l+1, r+1
    
    if h == s == 0:
        print("none")
    elif h == s:
        print("unsure")
    elif h > s:
        print("happy")
    else:
        print("sad")
        


solve()

