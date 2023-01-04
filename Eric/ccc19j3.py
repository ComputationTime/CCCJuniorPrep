


N = int(input())

linelist = []


def check(linelist):
    output = ""
    counter = 0
    curr_letter = ""
    for i in linelist:
        counter += 1
        if curr_letter == "":
            curr_letter = i
            counter -= 1
        if curr_letter != i:
            output += (str(counter) + " " +str(curr_letter) + " ")
            curr_letter = i
            counter = 0

    output += (str(counter+1) + " " +str(curr_letter))
        
    return output

    




for i in range(N):
    line = input()
    print(check(line))
