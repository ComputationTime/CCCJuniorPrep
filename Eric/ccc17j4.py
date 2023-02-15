D = int(input())

hr = 12
min = 0
count = 0
full_loop = 31


def check(hr,min):
    time = []
    diff = []
    output = 1
    global count
    if hr < 10:
        time.append(hr)
    else:
        time.append(hr//10)
        time.append(hr%10)
    if min < 10:
        time.append(0)
        time.append(min)
    else:
        time.append(min//10)
        time.append(min%10)

    for i in range(len(time)-1):
        diff.append(time[i]-time[i+1])

    for i in range(len(diff)-1):
        if diff[i] != diff[i+1]:
            output = 0
    
    count += output
    
if D > 720:
    count += ((D//720)*full_loop)
    D %= 720


for i in range(D):
    min += 1
    if min == 60:
        min = 0
        hr +=1
    if hr == 13:
        hr = 1
    check(hr,min)

print(count)



    
    