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

if currentMinute < 10: #if the current minute is less than 10, add a zero to the beginning
    print("0", end = "")
print(currentMinute, end = "") #make sure the minute is an integer as it could be ex. 24.0