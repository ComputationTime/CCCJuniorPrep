currentHour, currentMinute = map(int, input().split(":")) 

for minutesElapsed in range(120):  
    if (currentHour >= 7 and currentHour < 10) or (currentHour >= 15 and currentHour < 19): 
        currentMinute += 2 
    else:
        currentMinute += 1

    if currentMinute >= 60:
        currentMinute -= 60
        currentHour += 1
    if currentHour == 24: 
        currentHour -= 24


if currentHour < 10: 
    print("0", end = "")
print(currentHour, end = ":") 

if currentMinute < 10: 
    print("0", end = "")
print(currentMinute, end = "") 