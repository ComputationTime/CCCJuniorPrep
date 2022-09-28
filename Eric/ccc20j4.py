
t = input()
s = input()

answer = "no"

shiftedlist = []

shift = list(s)
shifter = ""


for i in range(len(s)):
    shift.append(shift[0])
    shift.pop(0)
    for i in shift:
        shifter = (shifter) + (i)
    shiftedlist.append(shifter)
    shifter = ""


for i in shiftedlist:
    if i in t:
        answer = "yes"

print(answer)


    

